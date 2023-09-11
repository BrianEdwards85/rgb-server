from ariadne import QueryType, load_schema_from_path, make_executable_schema
from ariadne.asgi import GraphQL
from .resolver import Resolver


def graph_api():
    type_defs = load_schema_from_path("./src/gql/")

    query = QueryType()
    r = Resolver("Hello?", query)

    schema = make_executable_schema(type_defs, query)
    app = GraphQL(schema, debug=True)

    return app
