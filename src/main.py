import asyncio
import uvicorn
from typing import Union
from fastapi import FastAPI, APIRouter
from models import Colors
from lights import Lights
from gql import graph_api


class Hello:
    def __init__(self, lights: Lights) -> None:
        self.lights = lights
        self.router = APIRouter()
        self.router.add_api_route("/", self.read_root, methods=["get"])
        self.router.add_api_route("/", self.post_root, methods=["post"])
        self.router.add_api_route("/items/{item_id}", self.read_item, methods=["get"])

    def read_root(self) -> dict[str, str]:
        return {"Hello": "World!"}

    def read_item(self, item_id: int, q: Union[str, None] = None):
        return {"item_id": item_id, "q": q}

    def post_root(self, colors: Colors):
        self.lights.set_pixels(colors)
        return {"colors": colors}


def api(lights: Lights):
    app = FastAPI()

    hello = Hello(lights)
    app.include_router(hello.router)
    app.mount("/graphql/", graph_api())

    return app


async def main(lights: Lights):
    config = uvicorn.Config(
        lambda: api(lights), port=5000, host="0.0.0.0", log_level="info", factory=True
    )
    server = uvicorn.Server(config)
    await server.serve()


if __name__ == "__main__":
    lights = Lights(144)

    asyncio.run(main(lights))
