from aiohttp import web
from lights import Lights
import logging

lights = Lights(144)


async def pj(request):
    try:
        data = await request.json()
    except Exception as e:
        raise web.HTTPBadRequest(text="Invalid request") from e
    try:
        color = data.get("color", 0)
        offset = data.get("offset", 0)
        count = data.get("count", 0)
        lights.set_pixels(offset, count, color)
        text = "Hello!"
    except (TypeError, ValueError) as e:
        logging.warning(e)
        raise web.HTTPBadRequest(text="Invalid name") from e
    return web.Response(text=text)


async def handle(request):
    name = request.match_info.get("name", "Anonymous")
    text = "Hello, " + name
    return web.Response(text=text)


def main():
    app = web.Application()
    app.add_routes(
        [web.get("/", handle), web.get("/{name}", handle), web.post("/", pj)]
    )
    web.run_app(app)


if __name__ == "__main__":
    main()
