from fastapi import FastAPI, Request
from starlette.responses import JSONResponse
from typing import Optional

class UserNameNoneException(Exception):
    def __init__(self, username: str):
        self.username = username

app = FastAPI()

@app.exception_handler(UserNameNoneException)
async def username_none_expection_handler(request: Request, exception: UserNameNoneException):
    return JSONResponse(status_code=404, content={"message": f"{exception.username} username is not valid"})

@app.get("/")
async def read_status(username: Optional[str]):
    if(username == "Sumit"):
        raise UserNameNoneException(username=username)
    return {"username": username, "status": "online"}
