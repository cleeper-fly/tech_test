import itertools
from typing import Any

from sqlalchemy import Result, TextClause, text

from app.api.dtos import Gene
from app.lib.classes import SQLAlchemySessionBaseUseCase


class GetInfoByGeneSymbol(SQLAlchemySessionBaseUseCase):
    def __init__(self, gene_symbol: str):
        super().__init__()
        self.gene_symbol = gene_symbol

    async def execute(self) -> list[Gene]:
        async with self._session_maker() as session:
            rows: Result[Any] = await session.execute(self.statement, {'gene_symbol': self.gene_symbol})

        return [
            Gene(gene_symbol=key[0], gene_stable_id=key[1], transcript_ids=[group[2] for group in list(g)])
            for key, g in itertools.groupby(rows, key=lambda x: (x[0], x[1]))
        ]

    @property
    def statement(self) -> TextClause:
        return text(
            '''
            SELECT gene.symbol AS gene_symbol, gene.stable_id AS gene_stable_id, transcript.stable_id
            FROM gene
            JOIN transcript ON gene.gene_id = transcript.gene_id
            WHERE gene.symbol = :gene_symbol
            '''
        )
