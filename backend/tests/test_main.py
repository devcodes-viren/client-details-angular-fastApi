from collections.abc import Generator

import pytest
from fastapi import HTTPException
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from main import get_client, health_check, list_clients
from models import Client


@pytest.fixture
def db_session() -> Generator[Session, None, None]:
    engine = create_engine("sqlite:///:memory:")
    Client.metadata.create_all(engine)
    session_factory = sessionmaker(bind=engine)
    session = session_factory()
    session.add_all(
        [
            Client(
                id=1,
                client_name="Alicia Johnson",
                email="alicia.johnson@example.com",
                phone="+1-555-0101",
                company="Northwind Labs",
                city="Seattle",
                status="active",
            ),
            Client(
                id=2,
                client_name="Marcus Chen",
                email="marcus.chen@example.com",
                phone="+1-555-0102",
                company="BrightPeak",
                city="Austin",
                status="pending",
            ),
        ]
    )
    session.commit()

    try:
        yield session
    finally:
        session.close()
        engine.dispose()


def test_health_check():
    assert health_check() == {"status": "ok"}


def test_list_clients_returns_all_clients(db_session: Session):
    clients = list_clients(db_session)

    assert len(clients) == 2
    assert clients[0]["client_name"] == "Alicia Johnson"
    assert clients[1]["status"] == "pending"


def test_get_client_returns_matching_client(db_session: Session):
    client = get_client(2, db_session)

    assert client["id"] == 2
    assert client["email"] == "marcus.chen@example.com"


def test_get_client_raises_404_for_unknown_id(db_session: Session):
    with pytest.raises(HTTPException) as error:
        get_client(999, db_session)

    assert error.value.status_code == 404
    assert error.value.detail == "Client not found"
