from ariadne import QueryType, load_schema_from_path, make_executable_schema
from ariadne.asgi import GraphQL
from .resolver import Query, MutationResolver


def graph_api():
    type_defs = load_schema_from_path("./src/gql/")

    query_resolver = Query("Hi!")
    query = query_resolver.query
    mutation_resolver = MutationResolver()
    mutations = mutation_resolver.mutation

    schema = make_executable_schema(type_defs, query, mutations)
    app = GraphQL(schema, debug=True)

    return app
