from pydantic import BaseModel, Field

class ResourceId(BaseModel):
    id: int

    class Config:
        orm_mode = True

class User(BaseModel):
    id: int
    first_name: str
    last_name: str
    username: str
    score: int

    class Config:
        orm_mode = True

class QuizCreate(BaseModel):
    question: str = Field(..., title="퀴즈 질문", example="대한민국의 수도는?")
    content: str = Field(..., title="퀴즈 내용", example="서울 인천 부산")
    answer: str = Field(..., title="정답", example="1")

class Quiz(QuizCreate):
    id: int

    class Config:
        orm_mode = True