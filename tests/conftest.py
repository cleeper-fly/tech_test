import pytest
from fastapi import FastAPI
from starlette.testclient import TestClient

from app.core.settings import get_settings
from app.main import create_app

settings = get_settings()


@pytest.fixture
def test_app() -> FastAPI:
    return create_app()


@pytest.fixture
def test_client(test_app: FastAPI) -> TestClient:
    return TestClient(test_app)
