from fastapi import FastAPI
from fastapi_pagination import add_pagination

from src.api.v1.routes import routers as v1_routers
from src.core.container import Container


app = FastAPI()

app.include_router(v1_routers, prefix="/api/v1")

container = Container()
add_pagination(app)


@app.get("/")
async def root():
    return {"Hello": "World"}
