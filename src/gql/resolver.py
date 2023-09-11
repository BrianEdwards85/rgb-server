from ariadne import QueryType


class Resolver:
    def __init__(self, name: str, query: QueryType) -> None:
        self.name = name
        query.set_field("hello", self.resolve_hello)

    def resolve_hello(self, *_):
        return self.name
