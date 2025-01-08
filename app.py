import strawberry
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from typing import List, Optional

users = [
    {"id": 1, "name": "John Doe", "email": "john@example.com"},
    {"id": 2, "name": "Jane Doe", "email": "jane@example.com"},
    {"id": 3, "name": "Alice Smith", "email": "alice@example.com"},
    {"id": 4, "name": "Bob Johnson", "email": "bob@example.com"},
    {"id": 5, "name": "Charlie Brown", "email": "charlie@example.com"},
    {"id": 6, "name": "David Williams", "email": "david@example.com"},
    {"id": 7, "name": "Emily Davis", "email": "emily@example.com"},
    {"id": 8, "name": "Frank Miller", "email": "frank@example.com"},
    {"id": 9, "name": "Grace Lee", "email": "grace@example.com"},
    {"id": 10, "name": "Henry Wilson", "email": "henry@example.com"}
]

books = [
    {"title": "Python Basics", "author": "John Doe"},
    {"title": "FastAPI for Beginners", "author": "Jane Doe"}
]
datas = [
    {"name":"rohan",
     "com_ca":9643}
]

@strawberry.type
class Data:
    name:str
    com_ca:int

@strawberry.type
class User:
    id: int
    name: str
    email: str

@strawberry.type
class Book:
    title: str
    author: str

@strawberry.type
class SearchResult:
    title: str
    description: str


@strawberry.type
class Query:
    @strawberry.field
    def hello(self) -> str:
        return "Hello, World!"

    @strawberry.field
    def users(self) -> List[User]:
        return [User(**user) for user in users]  # Fetch all users

    @strawberry.field
    def books(self) -> List[Book]:
        return [Book(**book) for book in books]
    @strawberry.field
    def data(self) -> List[Data]:
        return [Data(**data) for data in datas]
    @strawberry.field
    def searchs(self, query: str) -> List[SearchResult]:
        return [
            SearchResult(title="Python Basics", description="Learn Python basics."),
            SearchResult(title="FastAPI for Beginners", description="An introduction to FastAPI.")
        ]
app = FastAPI()
graphql_app = GraphQLRouter(schema=strawberry.Schema(query=Query))
app.include_router(graphql_app, prefix="/graphql")
