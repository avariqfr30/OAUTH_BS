import fastapi as _fastapi
import fastapi.security as _security

import sqlalchemy.orm as _orm
import passlib.hash as _hash
import database as _database
import models as _models
import schemes as _schemes

def create_database():
    return _database.Base.metadata.create_all(bind=_database.engine)

def get_db():
    db =_database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

async def creare_user(user: _schemes.userCreate, db: _orm.Session):
    user_obj = _models.User(
        email = user.email, 
        hashed_password = _hash.bcrypt.hash(user.hashed_password)
    )
    db.add(user_obj)
    db.commit()
    db.refresh(user_obj)
    return user_obj
