from ariadne import QueryType, MutationType
from models import Colors


class Query:
    def __init__(self, name: str) -> None:
        self.query = QueryType()
        self.name = name
        self.query.set_field("hello", self.resolve_hello)

    def resolve_hello(self, *_):
        return self.name


class MutationResolver:
    def __init__(self) -> None:
        self.mutation = MutationType()
        self.mutation.set_field("greet", self.resolve_greet)
        self.mutation.set_field("display", self.resolve_display)

    def resolve_greet(self, _, info, name: str):
        return f"Hello {name}"

    def resolve_display(self, _, info, input: dict):
        colors = Colors(**input)
        print(colors.model_dump())

        return "0"


class Resolver:
    def __init__(self, name: str, query: QueryType) -> None:
        self.name = name
        query.set_field("hello", self.resolve_hello)

    def resolve_hello(self, *_):
        return self.name
