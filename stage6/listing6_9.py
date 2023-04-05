""" Листинг 6.9 Распараллеливание операции reduce."""
import asyncio
import concurrent.futures
import functools
import time
from typing import Dict, List


def partition(data: List[str], chunk_size: int):
    for i in range(0, len(data), chunk_size):
        yield data[i:i + chunk_size]


def map_frequencies(chunk: List[str]) -> Dict[str, int]:
    counter: Dict[str, int] = {}
    for line in chunk:
        word, _, count, _ = line.split("\t")
        if counter.get(word):
            counter[word] = counter[word] + int(count)
        else:
            counter[word] = int(count)

    return counter


def merge_dictionares(first: Dict[str, int],
                      second: Dict[str, int]) -> Dict[str, int]:
    merged = first
    for key in second:
        if key in merged:
            merged[key] = merged[key] + second[key]
        else:
            merged[key] = second[key]

    return merged


async def reduce(loop, pool, counters, chunk_size) -> Dict[str, int]:
    chunks: List[List[Dict]] = list(partition(counters, chunk_size))
    reducers = []
    while len(chunks[0]) > 1:
        for chunk in chunks:
            reducer = functools.partial(
                functools.reduce, merge_dictionares, chunk)
            reducers.append(loop.run_in_executor(pool, reducer))
        reducer_chunks = await asyncio.gather(*reducers)
        chunks = list(partition(reducer_chunks, chunk_size))
        reducers.clear()

    return chunks[0][0]

async def main(partition_size: int):
    with open("stage6/googlebooks-eng-all-1gram-20120701-a.txt", encoding="utf-8") as f:
        contents = f.readlines()
        loop = asyncio.get_running_loop()
        tasks = []
        start = time.time()
        with concurrent.futures.ProcessPoolExecutor() as pool:
            for chunk in partition(contents, partition_size):
                tasks.append(loop.run_in_executor(
                    pool, functools.partial(
                        map_frequencies, chunk)))

        intermediate_results = await asyncio.gather(*tasks)
        final_result = await reduce(loop, pool, intermediate_results, 500)
        print(f"Aardvark встречается {final_result['Aardvark']} раз.")

        end = time.time()

        print(f"Время MapReduce: {end - start:.4f} секунд.")

if __name__ == "__main__":
    asyncio.run(main(partition_size=60000))
