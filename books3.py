from typing import Optional
from uuid import UUID
from fastapi import FastAPI, Form, Header, Request
from pydantic import BaseModel
from starlette.responses import JSONResponse

class NoBookFoundException(Exception):
    def __init__(self, book_id):
        self.book_id = book_id

app = FastAPI()

@app.exception_handler(NoBookFoundException)
def no_book_found_exception_handler(request: Request, exception:NoBookFoundException):
    return JSONResponse(status_code=404, content={"message": f"{exception.book_id} book is not available in DB."})

BOOKS = []

class Book(BaseModel):
    id: UUID
    title: str

@app.get("/")
async def read_all_books():
    initialize_books()
    return BOOKS

@app.post("/book/login")
async def create_book_login(book_id: int, username: Optional[str] = Header(None), password: Optional[str] = Header(None)):
    print(book_id)
    if username == "A" and password == "A" and BOOKS[book_id]:
        return BOOKS[book_id]
    raise NoBookFoundException(book_id=book_id)

def initialize_books():
    book1 = Book(id="812f3c2f-cded-40c3-b355-37ceafdb32d5", title="book 1")
    book2 = Book(id="712f3c2f-cded-40c3-b355-37ceafdb32d5", title="book 2")
    book3 = Book(id="612f3c2f-cded-40c3-b355-37ceafdb32d5", title="book 3")
    book4 = Book(id="512f3c2f-cded-40c3-b355-37ceafdb32d5", title="book 4")
    BOOKS.append(book1)
    BOOKS.append(book2)
    BOOKS.append(book3)
    BOOKS.append(book4)