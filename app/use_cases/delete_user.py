from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.repositories.UserRepository import UserRepository


class DeleteUser:
    def __init__(self, session: Session):
        self.repository = UserRepository(session)

    def execute(self, id: int):
        user = self.repository.find(id)
        if user is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found",
            )
        self.repository.delete(id)
