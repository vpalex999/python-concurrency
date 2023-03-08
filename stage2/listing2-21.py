""" Листинг 2.21 Создание цикла событий вручную."""
import asyncio


async def main():
    await asyncio.sleep(1)

loop = asyncio.new_event_loop()

try:
    loop.run_until_complete(main())
finally:
    loop.close()
    print("loop was close.")
