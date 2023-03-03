""" Снятие задачи."""
import asyncio
from asyncio import CancelledError

from util.delay_functions import delay


async def main():
    long_task = asyncio.create_task(delay(3))

    second_elapsed = 0

    while not long_task.done():
        print("Задача не закончилась, следующая проверка через секунду.")
        await asyncio.sleep(1)
        second_elapsed = second_elapsed + 1

        if second_elapsed == 5:
            long_task.cancel()

    try:
        await long_task
    except CancelledError:
        print("Наша задача была снята.")

asyncio.run(main())
