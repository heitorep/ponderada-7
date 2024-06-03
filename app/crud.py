from sqlalchemy.orm import Session
from . import models, schemas

def create_story(db: Session, story: schemas.StoryCreate):
    db_story = models.Story(title=story.title, description=story.description, category=story.category)
    db.add(db_story)
    db.commit()
    db.refresh(db_story)
    return db_story

def get_stories(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Story).offset(skip).limit(limit).all()

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(email=user.email, hashed_password="hashed_" + user.password, is_active=True)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()
