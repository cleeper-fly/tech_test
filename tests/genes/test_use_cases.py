import pytest
from pytest_mock import MockerFixture

from app.api.dtos import Gene
from app.api.use_cases import GetInfoByGeneSymbol
from app.core.db_config import AsyncSessionMaker

session_maker = AsyncSessionMaker


@pytest.mark.asyncio
async def test_use_case_with_data(mocker: MockerFixture):
    mocker.patch(
        'sqlalchemy.ext.asyncio.session.AsyncSession.execute',
        return_value=[
            ('gene_symbol', 'stable_id', 'transcript_id'),
            ('gene_symbol', 'stable_id', 'another_transcript_id'),
        ],
    )
    data = await GetInfoByGeneSymbol(gene_symbol='gene_symbol').execute()
    assert data == [
        Gene(
            **{
                'gene_symbol': 'gene_symbol',
                'gene_stable_id': 'stable_id',
                'transcript_ids': ['transcript_id', 'another_transcript_id'],
            }
        )
    ]


@pytest.mark.asyncio
async def test_use_case_no_data(mocker: MockerFixture):
    mocker.patch('sqlalchemy.ext.asyncio.session.AsyncSession.execute', return_value=[])
    data = await GetInfoByGeneSymbol(gene_symbol='gene_symbol').execute()
    assert data == []
