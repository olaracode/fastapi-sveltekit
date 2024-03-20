from pydantic import BaseModel

# Pydantic Schemas for src.models:User


class BaseUser(BaseModel):
    email: str


class UserCreate(BaseUser):
    password: str


class UserInDB(BaseUser):
    id: int

    class Config:
        from_attributes = True
