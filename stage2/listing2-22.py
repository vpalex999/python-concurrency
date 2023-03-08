""" Листинг 2.22 Получение доступа к циклу событий."""
import asyncio

from util.delay_functions import delay


def call_later():
    print("Меня вызовут в ближайшем будущем!")


async def main():
    loop = asyncio.get_running_loop()
    loop.call_soon(call_later)
    await delay(1)


asyncio.run(main())
