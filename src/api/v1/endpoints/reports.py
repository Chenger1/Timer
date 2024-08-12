from fastapi import (
    APIRouter,
    Depends
)
from dependency_injector.wiring import (
    inject,
    Provide
)


router = APIRouter(prefix="/reports", tags=["reports"])



