from fastapi import FastAPI
from app.routers import user
from app.db.database import Base, engine
from app.routers import user
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI(
    title="First API",
    description="My first api with FastAPI",
    version="1.0"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user.router)

Base.metadata.create_all(bind=engine)


@app.get("/")
def index():
    return  {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, port=8000)