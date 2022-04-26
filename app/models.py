from sqlalchemy import (
    Column, 
    Integer, 
    String, 
    BigInteger, 
    DateTime, 
    Text
)
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime,timezone


from app.database import Base

class BaseMixin:

    now = datetime.now(timezone.utc)

    id = Column(BigInteger, primary_key=True, index=True)
    created_at = Column(DateTime, nullable=False, default=now)
    updated_at = Column(DateTime, nullable=False, default=now, onupdate=now)

class User(BaseMixin, Base):
    __tablename__ = "user"

    quiz_id = Column(Integer, ForeignKey("quiz.id"), nullable=True)
    username = Column(String(100), default="")
    first_name = Column(String(100))
    last_name = Column(String(100))
    score = Column(Integer, default=0)

    quiz = relationship("Quiz", back_populates='current_users', uselist=False)

class Quiz(BaseMixin, Base):
    __tablename__ = "quiz"

    question = Column(Text, nullable=False)
    content = Column(Text, nullable=False)
    answer = Column(BigInteger, nullable=False)

    current_users = relationship("User", back_populates="quiz")