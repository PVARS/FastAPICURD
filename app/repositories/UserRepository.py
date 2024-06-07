from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session

from app.models.user import User


class UserRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, user: User):
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)

    def find(self, user_id) -> User | None:
        try:
            return self.session.query(User).filter(User.id == user_id).one()
        except NoResultFound:
            return None

    def find_user_already_exists(self, email: str, user_name: str) -> User | None:
        try:
            return self.session.query(User).filter(User.email == email, User.user_name == user_name).one()
        except NoResultFound:
            return None

    def find_user_by_user_name(self, user_name: str) -> User | None:
        try:
            return self.session.query(User).filter(User.user_name == user_name).one()
        except NoResultFound:
            return None

    def find_users(self) -> list[User]:
        return self.session.query(User).all()

    def update(self, id: int, user_update: User):
        user = self.session.query(User).filter(User.id == id).first()
        user.user_name = user_update.user_name
        user.email = user_update.email
        user.gender = user_update.gender
        user.first_name = user_update.first_name
        user.last_name = user_update.last_name

        self.session.commit()

    def delete(self, id: int):
        user = self.session.query(User).filter(User.id == id).first()
        user.delete()

        self.session.commit()
