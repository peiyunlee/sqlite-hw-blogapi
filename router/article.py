from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from router.schemas import ArticleRequestSchema, ArticleResponseSchema, LikeRequestSchema
from router.schemas import LikeResponseSchema, CommentResponseSchema, CommentRequestSchema
from db.database import get_db
from db import db_article
from typing import List

router = APIRouter(
    prefix='/api/v1/articles',
    tags=['articles']
)


@router.post('', response_model=ArticleResponseSchema)
def post(request: ArticleRequestSchema, db: Session = Depends(get_db)):
    return db_article.post(db, request)


@router.get('/all', response_model=List[ArticleResponseSchema])
def get_all_articles(db: Session = Depends(get_db)):
    return db_article.get_all(db)


@router.get('/id/{article_id}', response_model=ArticleResponseSchema)
def get_article_by_id(article_id: int, db: Session = Depends(get_db)):
    return db_article.get_article_by_id(article_id=article_id, db=db)


@router.get("/category/{category}", response_model=List[ArticleResponseSchema])
def get_articles_by_category(category: str, db: Session = Depends(get_db)):
    return db_article.get_articles_by_category(category=category, db=db)


@router.get("/author/{author_id}", response_model=List[ArticleResponseSchema])
def get_articles_by_author_id(author_id: int, db: Session = Depends(get_db)):
    return db_article.get_articles_by_author_id(author_id=author_id, db=db)


@router.post('/like', response_model=LikeResponseSchema)
def like(request: LikeRequestSchema, db: Session = Depends(get_db)):
    return db_article.like(db, request)


@router.post('/comment', response_model=CommentResponseSchema)
def comment(request: CommentRequestSchema, db: Session = Depends(get_db)):
    return db_article.comment(db, request)
