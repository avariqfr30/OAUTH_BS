from typing import Annotated
from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer

import sqlalchemy.orm as _orm
import services as _services
import schemes as _schemes

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@app.get("/items/")
async def read_items(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"token": token}

@app.post("/api/users")
async def create_user(
    user: _schemes.UserCreate, db: _orm.Session = FastAPI.Depends(_services.get_db)
):
    user = await _services.creare_user(user, db)
    return await user