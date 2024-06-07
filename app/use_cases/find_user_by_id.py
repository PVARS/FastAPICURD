from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.models.user import User
from app.repositories.UserRepository import UserRepository


class FindUserById:
    def __init__(self, session: Session):
        self.repository = UserRepository(session)

    def execute(self, id: int) -> User | None:
        user = self.repository.find(id)
        if user is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found",
            )
        return user
