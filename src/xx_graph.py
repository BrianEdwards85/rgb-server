import asyncio
import uvicorn
from ariadne import QueryType, gql, make_executable_schema
from ariadne.asgi import GraphQL

type_defs = gql(
    """
    type Query {
        hello: String!
    }
"""
)


class GG:
    def __init__(self, name: str, query: QueryType) -> None:
        self.name = name
        query.set_field("hello", self.resolve_hello)

    def resolve_hello(self, *_):
        return self.name


def graph_api():
    query = QueryType()
    gg = GG("Hello?", query)

    schema = make_executable_schema(type_defs, query)
    app = GraphQL(schema, debug=True)

    return app


async def main():
    config = uvicorn.Config(
        graph_api, port=5001, host="0.0.0.0", log_level="info", factory=True
    )
    server = uvicorn.Server(config)
    await server.serve()


if __name__ == "__main__":
    asyncio.run(main())
