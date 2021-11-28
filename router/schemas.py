from pydantic import BaseModel
from typing import List


class ArticleRequestSchema(BaseModel):
    category: str
    title: str
    content: str
    image:str
    author_id: int


class UserRequestSchema(BaseModel):
    username: str
    email: str
    password: str
    is_admin: bool


class ArticleResponseSchema(ArticleRequestSchema):
    id: int
    author_id: int

    class Config():
        orm_mode = True


class UserResponseSchema(UserRequestSchema):
    id: int
    posted_articles: List[ArticleResponseSchema] = []

    class Config:
        orm_mode = True