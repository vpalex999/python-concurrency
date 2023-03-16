""" Листинг 4.10 wait ожидание всех задач по умолчанию."""
import asyncio
from aiohttp import ClientSession
from util.async_timer import async_timed
from util.aiohttp_util import fetch_status


@async_timed()
async def main():
    async with ClientSession() as session:
        fetchers = [
            asyncio.create_task(fetch_status(session, 'https://example.com')),
            asyncio.create_task(fetch_status(session, 'https://example.com'))]

        done, pending = await asyncio.wait(fetchers)

        print(f"Число завершившихся задач: {len(done)}")
        print(f"Число ожидающих задач: {len(pending)}")

        for done_task in done:
            print(await done_task)

asyncio.run(main())
