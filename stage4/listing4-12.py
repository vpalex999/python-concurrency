""" Листинг 4.12 Отмена работающих запросов при возникновении исключения."""
import asyncio
import logging
from util.async_timer import async_timed
from util.aiohttp_util import fetch_status
from aiohttp import ClientSession


@async_timed()
async def main():
    async with ClientSession() as session:
        fetchers = [
            asyncio.create_task(fetch_status(
                session, 'https://example.com', delay=3)),
            asyncio.create_task(fetch_status(
                session, 'https://example.com', delay=3)),
            asyncio.create_task(fetch_status(session, 'python://bad'))]

        done, pending = await asyncio.wait(fetchers, return_when=asyncio.FIRST_EXCEPTION)

        print(f"Число завершившихся задач: {len(done)}")
        print(f"Число ожидающих задач: {len(pending)}")

        for done_task in done:
            if done_task.exception() is None:
                print(done_task.result())
            else:
                logging.error(
                    "При выполнении запроса возникло исключение", exc_info=done_task.exception())

        for pending_task in pending:
            pending_task.cancel()

asyncio.run(main())
