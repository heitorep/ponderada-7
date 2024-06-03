import pytest
from httpx import AsyncClient
from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app as myapp
from app.models import Base
from ..app.main import app as myapp


# Configuração do banco de dados de teste
DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="module")
def app() -> FastAPI:
    return myapp

@pytest.fixture(scope="module")
async def client(app: FastAPI) -> AsyncClient:
    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client

@pytest.fixture(scope="function")
def db_session():
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=engine)
