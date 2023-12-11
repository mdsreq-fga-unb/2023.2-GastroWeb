from asyncio import run

from database.connection import engine
from database.models import Base
from views.post_recipes import popula_bd

from database.models import *


async def create_database():
    async with engine.begin() as connection:
        #await connection.run_sync(Base.metadata.drop_all)
        await connection.run_sync(Base.metadata.create_all)


if __name__ == "__main__":
    run(create_database())
