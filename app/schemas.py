from pydantic import BaseModel
from uuid import UUID


class UserBase(BaseModel):
    first_name: str
    last_name: str
    email: str
    user_name: str
    gender: int


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: UUID

    class Config:
        orm_mode = True
