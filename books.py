from typing import Optional
from fastapi import FastAPI
from enum import Enum

app = FastAPI()

BOOKS = {
    "book_1":{"title": "Book 1", "author": "Author 1"},
    "book_2":{"title": "Book 2", "author": "Author 2"},
    "book_3":{"title": "Book 3", "author": "Author 3"},
    "book_4":{"title": "Book 4", "author": "Author 4"},
}

# READ

@app.get("/")
def read_all_books(skip_book: Optional[str] = None):
    if skip_book:
        new_books = BOOKS.copy()
        del new_books[skip_book]
        return new_books
    return BOOKS

# Path Parameter
@app.get("/{book_name}")
def read_book(book_name: str):
    return BOOKS[book_name]

# Enumerated Path Parameter
class Direction(str, Enum):
    north = "NORTH"
    south = "SOUTH"
    east = "EAST"
    west = "WEST"

@app.get("/directions/{direction}")
def get_direction(direction: Direction):
    if direction == Direction.north:
        return {"direction": direction, "sub": "UP"}
    if direction == Direction.south:
        return {"direction": direction, "sub": "DOWN"}
    if direction == Direction.west:
        return {"direction": direction, "sub": "LEFT"}
    return {"direction": direction, "sub": "RIGHT"}

# end

# CREATE

@app.post("/")
async def create_book(title: str, author: str):
    if len(BOOKS) > 0:
        current_book_id = 0
        for book in BOOKS:
            x = int(book.split("_")[-1])
            if(x > current_book_id):
                current_book_id = x
    BOOKS[f"book_{current_book_id + 1}"] = {"title": title, "author": author}
    return BOOKS[f"book_{current_book_id + 1}"]

# end

# UPDATE

@app.put("/{book_name}")
async def update_book(book_name: str, title:str, author: str):
    BOOKS[book_name] = {"title": title, "author": author}
    return {"title": title, "author": author}

# end

# DELETE

@app.delete("/{book_name}")
async def delete_book(book_name: str):
    del BOOKS[book_name]
    return f'{book_name} deleted.'

# end

# assignment 1
'''
1. Create a new read book function that uses query params instead of path params.
2. Create a new delete book function that use query params instead of path params.
'''

@app.get("/assignment/")
def read_book(book_name: str):
    return BOOKS[book_name]

@app.delete("/assignment/")
def delete_book(book_name: str):
    del BOOKS[book_name]
    return BOOKS