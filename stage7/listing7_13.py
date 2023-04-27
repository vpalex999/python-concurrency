""" Листинг 7.13 Класс нагрузочного тестирования для программы на Tkinter."""
import asyncio
from asyncio import futures
from concurrent.futures import Future
from asyncio import AbstractEventLoop
from typing import Callable, Optional
from aiohttp import ClientSession


class StressTest:
    def __init__(
            self, loop: AbstractEventLoop, url: str, total_requests: int,
            callback: Callable[[int, int],
                               None]) -> None:
        self._completed_requests: int = 0
        self._load_test_future: Optional[Future] = None
        self._loop = loop
        self._url = url
        self._total_requests = total_requests
        self._callback = callback
        self._refresh_rate = total_requests // 100

    def start(self) -> None:
        if self._load_test_future:
            future = asyncio.run_coroutine_threadsafe(
                self._make_requests(), self._loop)

            self._load_test_future = future

    def cancel(self) -> None:
        if self._load_test_future is not None:
            self._loop.call_soon_threadsafe(self._load_test_future.cancel)

    async def _get_url(self, session: ClientSession, url: str):
        try:
            await session.get(url)
        except Exception as e:
            print(e)

        self._completed_requests = self._completed_requests + 1
        if self._completed_requests % self._refresh_rate == 0 or self._completed_requests == self._total_requests:
            self._callback(self._completed_requests, self._total_requests)

    async def _make_requests(self):
        async with ClientSession() as session:
            reqs = [
                self._get_url(session, self._url)
                for _ in range(self._total_requests)]

            await asyncio.gather(*reqs)
