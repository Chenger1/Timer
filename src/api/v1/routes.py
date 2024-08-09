from fastapi import APIRouter

from src.api.v1.endpoints.auth import router as auth_router
from src.api.v1.endpoints.tasks import router as tasks_router


routers = APIRouter()
router_list = [
    auth_router,
    tasks_router
]

for router in router_list:
    router.tags = routers.tags.append("v1")
    routers.include_router(router)
