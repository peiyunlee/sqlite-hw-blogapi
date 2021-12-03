from pydantic import BaseModel
from typing import List


class ArticleRequestSchema(BaseModel):
    category: str
    title: str
    content: str
    image: str
    author_id: int


class LikeRequestSchema(BaseModel):
    article_id: int
    owner_id: int


class CommentRequestSchema(BaseModel):
    article_id: int
    owner_id: int
    content: str


class UserRequestSchema(BaseModel):
    username: str
    email: str
    password: str
    is_admin: bool


class LikeResponseSchema(LikeRequestSchema):
    id: int
    article_id: int
    owner_id: int

    class Config():
        orm_mode = True


class CommentResponseSchema(CommentRequestSchema):
    id: int
    article_id: int
    owner_id: int
    content: str

    class Config():
        orm_mode = True


class ArticleResponseSchema(ArticleRequestSchema):
    id: int
    author_id: int
    liked_owners: List[LikeResponseSchema] = []
    comment_owners: List[CommentResponseSchema] = []

    class Config():
        orm_mode = True


class UserResponseSchema(UserRequestSchema):
    id: int
    posted_articles: List[ArticleResponseSchema] = []
    liked_articles: List[LikeResponseSchema] = []
    comment_articles: List[CommentResponseSchema] = []

    class Config():
        orm_mode = True
