from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import Enum as SqlEnum

from src.database import get_db
from src.models.models import User, Profile
from src.redis import get_or_set_cache
"""
Should return the fields of the model and their data type. If one is a Enum, should return the possible values.
"""

models = [User, Profile]


def get_model_fields(model):
    fields = model.__table__.columns
    data_fields = []
    for field in fields:
        field_dict = {"name": field.name,
                      "data_type": field.type.python_type.__name__}
        if isinstance(field.type, SqlEnum):
            print(field.type.enums)
            field_dict["options"] = [e for e in field.type.enums]
            field_dict["data_type"] = "Enum"
        data_fields.append(field_dict)
    return data_fields


def validate_model(model_name):
    for model in models:
        print("MODEL: ", model.__name__)
        print("INCOMING: ", model_name)
        # transform to lowercase to avoid case sensitivity
        if model.__name__.lower() == model_name.lower():
            return model

    raise HTTPException(status_code=404, detail="Model not found")


router = APIRouter()


@router.get("/models")
async def get_models():
    return {model.__name__: get_model_fields(model) for model in models}


@router.get("/models/{model_name}")
async def get_model(model_name: str):
    for model in models:
        if model.__name__ == model_name:
            return get_model_fields(model)
    raise HTTPException(status_code=404, detail="Model not found")


@router.get("/get/{model_name}")
async def get_paginated(model_name: str, page: int = 1, limit: int = 10, db=Depends(get_db)):
    def get_model_page():
        model = validate_model(model_name)
        return db.query(model).limit(limit).offset((page - 1) * limit).all()
    return get_or_set_cache(f"admin:{model_name}:{page}:{limit}", get_model_page)


@router.get("/models/{model_name}/detail")
async def get_model_detail(model_name: str, db=Depends(get_db)):
    def get_model_details():
        model = validate_model(model_name)
        relationships = model.__mapper__.relationships
        return {"fields": get_model_fields(model), "relationships": [rel.key for rel in relationships]}

    return get_or_set_cache(f"admin:{model_name}:detail", get_model_details)
