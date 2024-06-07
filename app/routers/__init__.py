from fastapi import APIRouter
from app.routers import user
from app.routers import auth

router = APIRouter(prefix="/api")
router.include_router(user.router)
router.include_router(auth.router)
