import strawberry
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from pymongo import MongoClient
from typing import List, Union , Optional


client = MongoClient("mongodb://localhost:27017/")
db = client["arga"]
collection = db["data"]

@strawberry.type
class Student:
    _id: str
    name: str
    roll_no: str
    access_token :Optional[str]

@strawberry.type
class Query:
    @strawberry.field
    def get_students(self) -> List[Student]:
        students = collection.find()
        return [
            Student(
                _id=str(student["_id"]),
                name=student["name"],
                roll_no=str(student["roll_no"],),
                access_token=student.get("access_token"),
            )
            for student in students
        ]

schema = strawberry.Schema(query=Query)
app = FastAPI()
graphql_app = GraphQLRouter(schema)
app.include_router(graphql_app, prefix="/graphql")
