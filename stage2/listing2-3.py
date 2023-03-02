""" Выполнение сопрограммы."""
import asyncio


async def coroutine_add_one(number: int) -> int:
    return number + 1


coroutine_result = asyncio.run(coroutine_add_one(1))

print(
    f"Результат сопрограммы равен {coroutine_result}, а его тип равен {type(coroutine_result)}")
