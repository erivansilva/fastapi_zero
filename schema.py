from pydantic import BaseModel, EmailStr


class Message(BaseModel):
    message: str

    class Config:
        from_attributes = True


class UserSchema(BaseModel):
    username: str
    email: EmailStr
    password: str

    class Config:
        from_attributes = True


class UserPublic(BaseModel):
    username: str
    email: EmailStr
    id: int

    class Config:
        from_attributes = True


class UserList(BaseModel):
    users: list[UserPublic]

    class Config:
        from_attributes = True


class UserDB(UserSchema):
    id: int

    class Config:
        from_attributes = True
