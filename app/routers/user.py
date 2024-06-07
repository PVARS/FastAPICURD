from fastapi import APIRouter, Depends, status
from app.schemas import user
from sqlalchemy.orm import Session
from app.database import get_db
from app.use_cases.delete_user import DeleteUser
from app.use_cases.find_user_by_id import FindUserById
from app.use_cases.list_users import ListUsers
from app.use_cases.register_user import RegisterUser
from app.models.user import User
from app.use_cases.update_user import UpdateUser
from app.utils.util import Utils

router = APIRouter(
    prefix="/users",
    tags=["user"]
)


@router.post("/", response_model=user.User, status_code=status.HTTP_201_CREATED)
def register(user: user.UserCreate, db: Session = Depends(get_db)) -> User:
    use_case = RegisterUser(db)
    return use_case.execute(user)


@router.get("/", response_model=list[user.User], status_code=status.HTTP_200_OK)
def list_users(db: Session = Depends(get_db), current_user: str = Depends(Utils.get_current_user)):
    use_case = ListUsers(db)
    return use_case.execute()


@router.get("/{id}", response_model=user.User, status_code=status.HTTP_200_OK)
def find_user_by_id(id: int, db: Session = Depends(get_db),
                    current_user: str = Depends(Utils.get_current_user)) -> User:
    use_case = FindUserById(db)
    return use_case.execute(id)


@router.put("/{id}", response_model=user.User, status_code=status.HTTP_200_OK)
def update(id, user: user.UserUpdate, db: Session = Depends(get_db)) -> User:
    use_case = UpdateUser(db)
    return use_case.execute(id, user)


@router.delete("/{id}", response_model=dict, status_code=status.HTTP_200_OK)
def delete(id, db: Session = Depends(get_db)) -> User:
    use_case = DeleteUser(db)
    return use_case.execute(id)
