from dotenv import load_dotenv
import os

load_dotenv()

import models
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session, sessionmaker, selectinload

engine = create_engine(
    f"mariadb+mariadbconnector://{os.getenv('DB_USER')}:{os.getenv('DB_PASS')}@{os.getenv('DB_HOST')}/{os.getenv('DB_DBNAME')}", echo=True)

SessionLocal = sessionmaker(bind=engine, autoflush=False)

def run_in_session(func):
    def wrapper(*args, **kwargs):
        session = SessionLocal()
        try:
            result = func(session, *args, **kwargs)
            return result
        except Exception as e:
            print("Session error:")
            print(e)
            session.rollback()
            return None
        finally:
            session.close()
    return wrapper

@run_in_session
def get_all_projects(session: Session):
    stmt = select(models.Project).options(selectinload(models.Project.tags))
    scalars = session.scalars(stmt)
    return scalars.fetchall()

@run_in_session
def get_project_by_id(session: Session, id: int):
    stmt = select(models.Project).options(selectinload(models.Project.tags)).where(models.Project.id == id)
    scalar = session.scalar(stmt)
    return scalar

@run_in_session
def get_all_blogs(session: Session):
    stmt = select(models.Blog).options(selectinload(models.Blog.tags))
    scalars = session.scalars(stmt)
    return scalars.fetchall()

@run_in_session
def get_blog_by_id(session: Session, id: int):
    stmt = select(models.Blog).options(selectinload(models.Blog.tags)).where(models.Blog.id == id)
    scalar = session.scalar(stmt)
    return scalar

def close_session():
    engine.close()
