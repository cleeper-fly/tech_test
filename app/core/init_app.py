from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.core.settings import get_settings
from app.routes import api_v1_to_routers_map

settings = get_settings()


def init_middlewares(app: FastAPI) -> None:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*'],
    )


def register_routers(app: FastAPI) -> None:
    for api_v, routers in api_v1_to_routers_map.items():
        for router in routers:
            app.include_router(router, prefix=f'{settings.API_PREFIX}/{api_v}')
