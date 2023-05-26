import datetime as _dt
import pydantic as _pydantic

class _userBase(_pydantic.BaseModel):
    email: str

class userCreate(_userBase):
    hashed_password : str #This was a boolean, make it string so u can create new pass. Also it used "=" instead of ":" means its not changeable, fixed that too.

    class Config:
        orm_mode = True

class User(_userBase):
    id: int

    class Config:
        orm_mode = True