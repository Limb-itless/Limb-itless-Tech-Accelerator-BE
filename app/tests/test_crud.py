from collections.abc import Generator

import pytest
from sqlalchemy import create_engine
from sqlalchemy.pool import StaticPool
from sqlalchemy.orm import Session, sessionmaker

from app import crud, schemas
from app.database import Base

engine = create_engine(
    "sqlite:///:memory:",
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture()
def db() -> Generator[Session, None, None]:
    Base.metadata.create_all(bind=engine)
    session = TestingSessionLocal()
    try:
        yield session
    finally:
        session.close()
        Base.metadata.drop_all(bind=engine)


def test_create_and_get_item(db: Session) -> None:
    item = crud.create_item(db, schemas.ItemCreate(name="Socket liner", price=49.5))
    assert item.id is not None

    fetched = crud.get_item(db, item.id)
    assert fetched is not None
    assert fetched.name == "Socket liner"


def test_delete_item(db: Session) -> None:
    item = crud.create_item(db, schemas.ItemCreate(name="Test strap", price=9.99))
    assert crud.delete_item(db, item.id) is True
    assert crud.get_item(db, item.id) is None


def test_delete_missing_item_returns_false(db: Session) -> None:
    assert crud.delete_item(db, 12345) is False
