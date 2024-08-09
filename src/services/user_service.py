from src.services.base_service import BaseService
from src.models.user import User
from src.repositories.user_repository import UserRepository


class UserService(BaseService):
    def __init__(self, repository: UserRepository):
        super().__init__(repository)

    async def get_user_by_id(self, user_id: int) -> User:
        return await self._repository.get_by_id(user_id)
