from typing import Optional
from uuid import UUID
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

class Book(BaseModel):
    id: UUID
    title: str = Field(min_length=1)
    author: str = Field(min_length=1, max_length=100)
    description: Optional[str] = Field(title="Description of book", max_length=100, min_length=1)
    ratings: int = Field(gt=-1, lt=101)

    class Config:
        schema_extra = {
            "example": {
                "id": "1274f460-08a4-49bb-8a52-a07d443698d0",
                "title": "Computer Science Pro",
                "author": "Jack Daniel",
                "description": "Get the best out of the book.",
                "ratings": 7,
            }
        }

BOOKS = []

@app.get("/")
async def read_all_books(books_to_return: Optional[int] = None):
    if len(BOOKS) < 1:
        initialize_book_api()

    if books_to_return and len(BOOKS) >= books_to_return > 0:
        i = 1
        new_book = []
        while i <= books_to_return:
            new_book.append(BOOKS[i - 1])
            i += 1
        return new_book 
    return BOOKS

@app.get("/books/{book_id}")
async def read_book(book_id: UUID):
    for x in BOOKS:
        if x.id == book_id:
            return x

@app.put("/{book_id}")
async def update_book(book_id: UUID, book: Book):
    counter = 0

    for x in BOOKS:
        counter += 1
        if x.id == book_id:
            BOOKS[counter - 1] = book
            return BOOKS[counter - 1]

@app.delete("/{book_id}")
async def delete_book(book_id: UUID):
    counter = 0

    for x in BOOKS:
        counter += 1
        if x.id == book_id:
            del BOOKS[counter - 1]
            return f'ID {book_id} deleted.'

@app.post("/")
async def create_book(book: Book):
    BOOKS.append(book)
    return book

def initialize_book_api():
    book_1 = Book(
        id="3274f460-08a4-49bb-8a52-a07d443698d0",
        title= "Book1",
        author= "Author1",
        description= "Description1",
        ratings=3,
    )
    book_2 = Book(
        id="2274f460-08a4-49bb-8a52-a07d443698d0", 
        title="Book2",
        author="Author2",
        description="Description2",
        ratings=8,
    )
    BOOKS.append(book_1)
    BOOKS.append(book_2)