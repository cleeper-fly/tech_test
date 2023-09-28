from abc import ABC, abstractmethod
from typing import Any

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from app.core.db_config import AsyncSessionMaker


class AbstractUseCase(ABC):
    @abstractmethod
    async def execute(self) -> Any:
        pass


class SQLAlchemySessionBaseUseCase(AbstractUseCase):
    def __init__(self) -> None:
        self._session_maker: async_sessionmaker[AsyncSession] = AsyncSessionMaker

    @abstractmethod
    async def execute(self) -> Any:
        pass
