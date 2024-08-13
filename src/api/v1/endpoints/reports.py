from typing import List

from fastapi import (
    APIRouter,
    Depends
)
from dependency_injector.wiring import (
    inject,
    Provide
)

from src.core.container import Container
from src.services import SummaryService
from src.schemas.reports import SummaryReport
from src.dependencies.security import require_permissions


router = APIRouter(prefix="/reports", tags=["reports"])


@router.get("/summary", dependencies=[Depends(require_permissions())], response_model=List[SummaryReport])
@inject
async def get_summary(service: SummaryService = Depends(Provide[Container.summary_service])):
    return await service.get_report()
