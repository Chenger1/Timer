from src.services.base_service import BaseService
from src.repositories import ClientsRepository
from src.schemas.clients import (
    ClientSchema,
    ClientResponseSchema
)
from src.models.clients import Clients
from src.validators.clients_validator import CreateClientValidator


class ClientsService(BaseService):
    def __init__(self, repository: ClientsRepository):
        super().__init__(repository)

    @classmethod
    def convert_model_to_schema(cls, model: Clients) -> ClientResponseSchema:
        return ClientResponseSchema(
            id=model.id,
            email=model.email,
            address=model.address,
            note=model.note,
            user_id=model.user_id,
            name=model.name,
        )

    async def create_client(self, schema: ClientSchema) -> ClientResponseSchema:
        await CreateClientValidator().validate(schema)
        client = Clients(**schema.dict())
        client = await self._repository.create(client)
        return self.convert_model_to_schema(client)
