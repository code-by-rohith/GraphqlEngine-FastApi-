from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
import strawberry
from typing import List


book_db = []

@strawberry.type
class Book:
    id: int
    title: str
    author: str


@strawberry.input
class BookInput:
    title: str
    author: str

@strawberry.type
class Query:
    @strawberry.field
    def get_books(self) -> List[Book]:
        return book_db

    @strawberry.field
    def get_book(self, id: int) -> Book:
        for book in book_db:
            if book.id == id:
                return book
        raise ValueError(f"Book with ID {id} not found.")


@strawberry.type
class Mutation:
    @strawberry.field
    def create_book(self, book: BookInput) -> Book:
        new_book = Book(id=len(book_db) + 1, title=book.title, author=book.author)
        book_db.append(new_book)
        return new_book

    @strawberry.field
    def update_book(self, id: int, book: BookInput) -> Book:
        for b in book_db:
            if b.id == id:
                b.title = book.title
                b.author = book.author
                return b
        raise ValueError(f"Book with ID {id} not found.")

    @strawberry.field
    def delete_book(self, id: int) -> str:
        global book_db
        book_db = [b for b in book_db if b.id != id]
        return f"Book with ID {id} deleted successfully."


schema = strawberry.Schema(query=Query, mutation=Mutation)
graphql_app = GraphQLRouter(schema)


app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")
