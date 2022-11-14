from uuid import UUID
from fastapi import FastAPI
from pydantic import BaseModel

class Book(BaseModel):
    id: UUID
    title: str
    author: str
    description: str
    rating: int

class BookNoRating(BaseModel):
    id: UUID
    title: str

app = FastAPI()

BOOKS = []

@app.get("/book/rating/{book_id}", response_model=BookNoRating)
async def read_book_no_rating(book_id: UUID):
    if len(BOOKS) == 0:
        new_book = Book(id="b75b49b2-dd48-4e81-be96-860834b163bc",
                        title="Book 1",
                        author="Author 1",
                        description="Description 1",
                        rating=100)
        BOOKS.append(new_book)
    for x in BOOKS:
        if x.id == book_id:
            return x