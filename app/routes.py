from types import MappingProxyType

from fastapi import APIRouter

from app.api.v1.api import router as gene_search_router

v1_routers: tuple[APIRouter, ...] = (gene_search_router,)


api_v1_to_routers_map: MappingProxyType[str, tuple[APIRouter, ...]] = MappingProxyType(
    {
        'v1': v1_routers,
    }
)
