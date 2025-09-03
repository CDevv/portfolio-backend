from dotenv import load_dotenv
import os

load_dotenv()

import models
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

engine = create_engine(
    f"mariadb+mariadbconnector://{os.getenv('DB_USER')}:{os.getenv('DB_PASS')}@{os.getenv('DB_HOST')}/{os.getenv('DB_DBNAME')}", echo=True)

session = Session(engine)

def get_all_projects():
    stmt = select(models.Project)
    scalars = session.scalars(stmt)
    return scalars.fetchall()

def get_project_by_id(id: int):
    stmt = select(models.Project).where(models.Project.id == id)
    scalar = session.scalar(stmt)
    return scalar

def get_all_blogs():
    stmt = select(models.Blog)
    scalars = session.scalars(stmt)
    return scalars.fetchall()

def get_blog_by_id(id: int):
    stmt = select(models.Blog).where(models.Blog.id == id)
    scalar = session.scalar(stmt)
    return scalar

def close_session():
    session.close()