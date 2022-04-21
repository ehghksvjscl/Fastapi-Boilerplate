from re import S
from urllib import response
from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session
from sqlalchemy import func

from typing import List

from app import models, schemas
from app.config import settings
from app.database import get_db
from app.lib.telegram import telegram, schema

router = APIRouter()


@router.get("", response_model=List[schemas.Quiz])
async def get_quiz_list(db: Session = Depends(get_db)):
    return db.query(models.Quiz).all()

@router.post("", response_model=schemas.ResourceId, status_code=201)
async def create_quiz(data: schemas.QuizCreate, db: Session = Depends(get_db)):
    row = models.Quiz(**data.dict())
    db.add(row)
    db.commit()

    return row

@router.get("/random", response_model=schemas.Quiz)
async def get_quiz_randomly(db: Session = Depends(get_db)):
    return db.query(models.Quiz).order_by(func.RAND()).first()
