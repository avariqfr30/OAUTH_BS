import datetime as _dt


class userBase(_pydantic.Basemodel):
    email: str

class userCreate(userBase):
    hashed_password =True

    class Config:
        orm_mode = True

class User(userBase):
    id: int

    class Config:
        orm_mode = True