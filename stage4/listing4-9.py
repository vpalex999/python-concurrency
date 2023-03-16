""" Листинг 4.9 Задание тайм-аута для as_completed."""
import asyncio
from aiohttp import ClientSession
from util.async_timer import async_timed
from util.aiohttp_util import fetch_status


@async_timed()
async def main():
    async with ClientSession() as session:
        fetchers = [
            fetch_status(session, 'https://example.com', 1),
            fetch_status(session, 'https://example.com', 10),
            fetch_status(session, 'https://example.com', 10)]

        for finished_task in asyncio.as_completed(fetchers, timeout=2):
            try:
                print(await finished_task)
            except asyncio.TimeoutError:
                print("Произошёл тайм-аут!")

        for task in asyncio.tasks.all_tasks():
            print(task)

asyncio.run(main())
