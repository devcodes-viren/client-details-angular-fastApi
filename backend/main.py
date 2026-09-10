import os
from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import select
from sqlalchemy.orm import Session

from database import Base, SessionLocal, engine, get_db
from models import Client


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    seed_clients()
    yield


app = FastAPI(title="Client Details API", version="1.0.0", lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:4200",
        "http://127.0.0.1:4200",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def seed_clients():
    db = SessionLocal()
    try:
        if db.query(Client).count() == 0:
            sample_clients = [
                Client(
                    client_name="Alicia Johnson",
                    email="alicia.johnson@example.com",
                    phone="+1-555-0101",
                    company="Northwind Labs",
                    city="Seattle",
                    status="active",
                ),
                Client(
                    client_name="Marcus Chen",
                    email="marcus.chen@example.com",
                    phone="+1-555-0102",
                    company="BrightPeak",
                    city="Austin",
                    status="pending",
                ),
                Client(
                    client_name="Sofia Patel",
                    email="sofia.patel@example.com",
                    phone="+1-555-0103",
                    company="RiverStone Group",
                    city="Chicago",
                    status="active",
                ),
            ]
            db.add_all(sample_clients)
            db.commit()
    finally:
        db.close()


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/clients")
def list_clients(db: Session = Depends(get_db)):
    result = db.execute(select(Client)).scalars().all()
    return [
        {
            "id": client.id,
            "client_name": client.client_name,
            "email": client.email,
            "phone": client.phone,
            "company": client.company,
            "city": client.city,
            "status": client.status,
        }
        for client in result
    ]


@app.get("/clients/{client_id}")
def get_client(client_id: int, db: Session = Depends(get_db)):
    client = db.get(Client, client_id)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    return {
        "id": client.id,
        "client_name": client.client_name,
        "email": client.email,
        "phone": client.phone,
        "company": client.company,
        "city": client.city,
        "status": client.status,
    }
