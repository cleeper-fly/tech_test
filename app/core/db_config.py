from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from app.core.settings import get_settings

settings = get_settings()


async_engine = create_async_engine(
    settings.DB_URI,
    pool_pre_ping=True,
)


AsyncSessionMaker = async_sessionmaker(
    bind=async_engine,
    expire_on_commit=False,
    autoflush=False,
    future=True,
)
