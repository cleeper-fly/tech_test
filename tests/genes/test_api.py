import pytest
from fastapi import FastAPI
from httpx import AsyncClient
from pytest_mock import MockerFixture

from app.api.dtos import Gene


@pytest.mark.asyncio
async def test_get_genes_null(mocker: MockerFixture, test_app: FastAPI):
    async with AsyncClient(app=test_app, base_url='http://test') as ac:
        mocker.patch('app.api.use_cases.GetInfoByGeneSymbol.execute')
        response = await ac.get('api/v1/genes?gene_symbol=ABC')
        assert response.status_code == 200
        assert response.json() == []


@pytest.mark.asyncio
async def test_get_genes_with_data(mocker: MockerFixture, test_app: FastAPI):
    mocker.patch(
        'app.api.use_cases.GetInfoByGeneSymbol.execute',
        return_value=[Gene(gene_symbol='TEST', gene_stable_id='TEST_STABLE_ID', transcript_ids=['TEST_TRANSCRIPT_ID'])],
    )
    async with AsyncClient(app=test_app, base_url='http://test') as ac:
        response = await ac.get('api/v1/genes?gene_symbol=ABC')
        assert response.status_code == 200
        assert response.json() == [
            {'gene_symbol': 'TEST', 'gene_stable_id': 'TEST_STABLE_ID', 'transcript_ids': ['TEST_TRANSCRIPT_ID']}
        ]
