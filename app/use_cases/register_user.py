from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate
from app.models.user import User
from passlib.context import CryptContext

from app.repositories.UserRepository import UserRepository

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class RegisterUser:
    def __init__(self, session: Session):
        self.repository = UserRepository(session)

    def execute(self, user_create: UserCreate) -> User:
        user = User(
            first_name=user_create.first_name,
            last_name=user_create.last_name,
            email=user_create.email,
            user_name=user_create.user_name,
            gender=user_create.gender,
            password=pwd_context.hash(user_create.password),
        )

        user_already_exists = self.repository.find_user_already_exists(user.email, user.user_name)
        if user_already_exists:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="User already exists",
            )

        self.repository.create(user)
        return user
