""" Листинг 4.6 Конкурентное выполнение запросов с по­мощью gather."""
import asyncio
import aiohttp
from aiohttp import ClientSession
from util.aiohttp_util import fetch_status
from util.async_timer import async_timed


@async_timed()
async def main():
    async with ClientSession() as session:
        urls = ["https://example.com" for _ in range(1000)]
        requests = [fetch_status(session, url) for url in urls]
        status_codes = await asyncio.gather(*requests)
        print(status_codes)


asyncio.run(main())
