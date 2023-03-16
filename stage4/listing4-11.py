""" Листинг 4.11 Обработка исключений при использовании wait."""
import asyncio
import logging
from util.async_timer import async_timed
from util.aiohttp_util import fetch_status
from aiohttp import ClientSession


@async_timed()
async def main():
    async with ClientSession() as session:
        fetchers = [
            asyncio.create_task(fetch_status(session, 'https://example.com')),
            asyncio.create_task(fetch_status(session, 'python://bad'))]

        done, pending = await asyncio.wait(fetchers)

        print(f"Число завершившихся задач: {len(done)}")
        print(f"Число ожидающих задач: {len(pending)}")

        for done_task in done:
            if done_task.exception() is None:
                print(done_task.result())
            else:
                logging.error("При выполнении запроса возникло исключение", exc_info=done_task.exception())

asyncio.run(main())
