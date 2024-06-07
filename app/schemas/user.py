from pydantic import BaseModel


class UserBase(BaseModel):
    first_name: str
    last_name: str
    email: str
    user_name: str
    gender: int
    password: str


class UserCreate(UserBase):
    pass


class UserUpdate(BaseModel):
    first_name: str
    last_name: str
    email: str
    user_name: str
    gender: int


class User(UserBase):
    id: int

    class Config:
        orm_mode = True
