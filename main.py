from fastapi import FastAPI

from src.api.v1.routes import routers as v1_routers
from src.core.container import Container


app = FastAPI()

app.include_router(v1_routers, prefix="/api/v1")

container = Container()


@app.get("/")
async def root():
    return {"Hello": "World"}
