""" Листинг 5.14 Простой асинхронный генератор."""
import asyncio
from util.delay_functions import delay
from util.async_timer import async_timed


async def positive_integers_async(until: int):
    for integer in range(1, until):
        await delay(integer)
        yield integer


@async_timed()
async def main():
    async_generator = positive_integers_async(3)

    async for number in async_generator:
        print(f"Получено число {number}")

asyncio.run(main())
