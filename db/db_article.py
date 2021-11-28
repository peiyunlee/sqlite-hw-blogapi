from fastapi import HTTPException, status
from router.schemas import ArticleRequestSchema
from sqlalchemy.orm.session import Session
from db.models import DbArticle


def post(db: Session, request: ArticleRequestSchema) -> DbArticle:
    new_article = DbArticle(
        category=request.category,
        title=request.title,
        content=request.content,
        image=request.image,
        author_id=request.author_id,
    )
    db.add(new_article)
    db.commit()
    db.refresh(new_article)
    return new_article


def get_all(db: Session):
    return db.query(DbArticle).all()


def get_article_by_id(article_id: int, db: Session) -> DbArticle:
    article = db.query(DbArticle).filter(DbArticle.id == article_id).first()
    if not article:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Article with id = {id} not found')
    return article


def get_articles_by_category(category: str, db: Session):
    article = db.query(DbArticle).filter(DbArticle.category == category).all()
    if not article:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Article with category = {id} not found')
    return article


def get_articles_by_author_id(author_id: int, db: Session):
    article = db.query(DbArticle).filter(DbArticle.author_id == author_id).all()
    if not article:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Article with category = {id} not found')
    return article
