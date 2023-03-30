""" Листинг 5.17 Получение заданного числа элементов с по­мощью асинхронного генератора."""
import asyncpg
import asyncio


async def take(generator, to_take: int):
    item_count = 0
    async for item in generator:
        if item_count > to_take - 1:
            return
        item_count = item_count + 1
        yield item


async def main():
    connection = await asyncpg.connect(host="127.0.0.1", port=5432, user="postgres", database="products", password="password")

    async with connection.transaction():
        query = "SELECT product_id, product_name FROM product"
        cursor = connection.cursor(query)

        async for product in take(cursor, 5):
            print(product)

        print("Получены первые 5 товаров!")

    await connection.close()

asyncio.run(main())
