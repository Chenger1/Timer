from typing import (
    List,
    Tuple
)

from src.services.base_service import BaseService
from src.repositories.tasks_repository import TasksRepository
from src.schemas.reports import SummaryReport


class SummaryService(BaseService):
    def __init__(self, repository: TasksRepository):
        super().__init__(repository)

    @classmethod
    def convert_model_to_schema(cls, model: Tuple) -> SummaryReport:
        return SummaryReport(
            date=model[0],
            total_earned=model[1] if model[1] is not None else 0,
        )

    async def get_report(self) -> List[SummaryReport]:
        res = await self._repository.get_summary_report()
        return [self.convert_model_to_schema(i) for i in res]
