from fastapi import (
    APIRouter,
    Depends
)
from dependency_injector.wiring import (
    inject,
    Provide
)

from src.core.container import Container
from src.services.clients_service import ClientsService
from src.schemas.clients import (
    ClientSchema,
    ClientResponseSchema
)
from src.dependencies.security import require_permissions


router = APIRouter(prefix="/clients", tags=["clients"])


@router.post("/create", dependencies=[], response_model=ClientResponseSchema)
@inject
async def create_client(client: ClientSchema, service: ClientsService = Depends(Provide[Container.clients_service])):
    return await service.create_client(client)
