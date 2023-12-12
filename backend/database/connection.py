from decouple import config

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker


DATABASE_URL = "postgresql://gastroweb:EjJ789coMnsE0mETtI7Py3uFWTfmHFpo@dpg-clrqfkfqd2ns73ds4n10-a.oregon-postgres.render.com/gastroweb"

engine = create_async_engine(DATABASE_URL)
async_session = sessionmaker(engine, class_=AsyncSession)
