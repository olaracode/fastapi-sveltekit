import os
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException
from jose import JWTError, jwt
from typing import Annotated, Union
from pydantic import BaseModel
from datetime import datetime, timedelta

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
TOKEN_KEY = os.environ.get("KEY")
REFRESH_KEY = os.environ.get("REFRESH_KEY")
ALGORITHM = os.environ.get("ALGORITHM")


class Token(BaseModel):
    access_token: str
    refresh_token: str


def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
    # Basic token
    try:
        to_encode = data.copy()
        expire = expires_delta if expires_delta else timedelta(minutes=15)
        expire = datetime.utcnow() + expire
        to_encode.update({"exp": expire})
        auth_token = jwt.encode(to_encode, TOKEN_KEY, algorithm=ALGORITHM)

        # refresh token
        refresh_expires = timedelta(days=30)
        refresh_to_encode = data.copy()
        refresh_to_encode.update({"exp": datetime.utcnow() + refresh_expires})
        refresh_token = jwt.encode(
            refresh_to_encode, REFRESH_KEY, algorithm=ALGORITHM)
        return {"access_token": auth_token, "refresh_token": refresh_token}
    except Exception as e:
        raise e


async def get_refresh_user(
    token: Annotated[str, Depends(oauth2_scheme)]
):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, REFRESH_KEY, algorithms=[ALGORITHM])
        if payload is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    return payload


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, TOKEN_KEY, algorithms=[ALGORITHM])
        print(payload)
        user = payload.get("user")
        if user is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    return user
