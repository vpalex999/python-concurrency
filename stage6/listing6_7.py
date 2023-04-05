""" Листинг 6.7 Синхронный подсчет частот слов, начинающихся буквой a."""
import time

freqs = {}

with open("stage6/googlebooks-eng-all-1gram-20120701-a.txt", encoding="utf-8") as f:
    start = time.time()

    for line in f:
        data = line.split("\t")
        word = data[0]
        count = int(data[2])
        if word in freqs:
            freqs[word] = freqs[word] + 1
        else:
            freqs[word] = 1

    end = time.time()
    print(f"{end - start:.4f}")


