from sqlalchemy.orm import Session

from app.repositories.UserRepository import UserRepository


class ListUsers:
    def __init__(self, session: Session):
        self.repository = UserRepository(session)

    def execute(self):
        return self.repository.find_users()
