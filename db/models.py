from .database import Base
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey


class DbArticle(Base):
    __tablename__ = 'article'
    id = Column(Integer, primary_key=True, index=True)
    category = Column(String)
    title = Column(String)
    content = Column(String)
    image = Column(String)
    author_id = Column(Integer, ForeignKey('user.id'))
    author = relationship('DbUser', back_populates='posted_articles')
    liked_owners = relationship('DbLike', back_populates='article')
    comment_owners = relationship('DbComment', back_populates='article')


class DbUser(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)
    is_admin = Column(Boolean)
    posted_articles = relationship('DbArticle', back_populates='author')
    liked_articles = relationship('DbLike', back_populates='owner')
    comment_articles = relationship('DbComment', back_populates='owner')


class DbLike(Base):
    __tablename__ = 'article_like'
    id = Column(Integer, primary_key=True, index=True)
    article_id = Column(Integer, ForeignKey('article.id'))
    article = relationship('DbArticle', back_populates='liked_owners')
    owner_id = Column(Integer, ForeignKey('user.id'))
    owner = relationship('DbUser', back_populates='liked_articles')


class DbComment(Base):
    __tablename__ = 'article_comment'
    id = Column(Integer, primary_key=True, index=True)
    content = Column(String)
    article_id = Column(Integer, ForeignKey('article.id'))
    article = relationship('DbArticle', back_populates='comment_owners')
    owner_id = Column(Integer, ForeignKey('user.id'))
    owner = relationship('DbUser', back_populates='comment_articles')
