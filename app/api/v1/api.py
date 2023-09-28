from fastapi import APIRouter, Query, status
from fastapi.responses import ORJSONResponse

from app.api.dtos import Gene
from app.api.use_cases import GetInfoByGeneSymbol

router = APIRouter(
    prefix='/genes',
    tags=['genes'],
    default_response_class=ORJSONResponse,
)


@router.get('', status_code=status.HTTP_200_OK)
async def get_genes(gene_symbol: str = Query(...)) -> list[Gene] | None:
    return await GetInfoByGeneSymbol(gene_symbol).execute()
