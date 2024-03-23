from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware

from src.database import SessionLocal, engine
from src.auth.routes import router as UserRouter
from src.admin.routes import router as AdminRouter

app = FastAPI()
origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:8000",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(UserRouter, prefix="/user", tags=["user"])
app.include_router(AdminRouter, prefix="/admin", tags=["admin"])


@app.get("/")
async def root():
    return {"message": "Hello World"}
