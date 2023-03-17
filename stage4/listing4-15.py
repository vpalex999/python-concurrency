""" Листинг 4.15 Использование тайм-аутов в wait."""
import asyncio
import logging
from util.async_timer import async_timed
from util.aiohttp_util import fetch_status
from aiohttp import ClientSession


@async_timed()
async def main():
    async with ClientSession() as session:
        pending = [
            asyncio.create_task(fetch_status(session, 'https://example.com')),
            asyncio.create_task(fetch_status(session, 'https://example.com')),
            asyncio.create_task(fetch_status(session, 'https://example.com', delay=3))]

        while pending:
            done, pending = await asyncio.wait(pending, timeout=1)

            print(f"Число завершившихся задач: {len(done)}")
            print(f"Число ожидающих задач: {len(pending)}")

            for done_task in done:
                print(await done_task)

asyncio.run(main())
