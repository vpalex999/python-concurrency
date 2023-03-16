""" Листинг 4.8 Использование as_completed."""
import asyncio
from aiohttp import ClientSession
from util.async_timer import async_timed
from util.aiohttp_util import fetch_status


@async_timed()
async def main():
    async with ClientSession() as session:
        fetchers = [
            fetch_status(session, 'https://example.com', 1),
            fetch_status(session, 'https://example.com', 1),
            fetch_status(session, 'https://example.com', 10)]

        for finished_task in asyncio.as_completed(fetchers):
            print(await finished_task)

asyncio.run(main())
