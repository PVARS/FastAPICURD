from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models import User
from app.repositories.UserRepository import UserRepository
from app.schemas.user import UserUpdate


class UpdateUser:
    def __init__(self, session: Session):
        self.repository = UserRepository(session)

    def execute(self, id: int, user_update: UserUpdate) -> User:
        user = self.repository.find(id)
        if user is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found",
            )
        user = User(
            id=user.id,
            user_name=user_update.user_name,
            email=user_update.email,
            first_name=user_update.first_name,
            last_name=user_update.last_name,
            gender=user_update.gender,
            password=user.password
        )
        self.repository.update(id, user)
        return user
