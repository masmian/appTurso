from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()
TURSO_DATABASE_URL = "libsql://fastapi-database-masmian.turso.io"
TURSO_AUTH_TOKEN = "eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJhIjoicnciLCJpYXQiOjE3MTM0ODAxNDAsImlkIjoiNWUzMTJhYjEtZjA5MS00MDZjLWE5YjgtOWEwOWNmZmRlZTU5In0.dwZXm16rwJtImyn0Qfjoo3cZJD6p5KCpWdEWWUzTJD_i9rPCsuAaaRyU2XaT882VaAkq_kh85MLgCMfZNooaAQ"

dbUrl = f"sqlite:///database.db"
#dbUrl = f"sqlite+{TURSO_DATABASE_URL}/?authToken={TURSO_AUTH_TOKEN}&secure=true"
engine = create_engine(dbUrl)
SesionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()

def get_db():
    db = SesionLocal()
    try:
        yield db
    finally:
        db.close()
