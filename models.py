import datetime
from typing import List
from sqlalchemy import Column, ForeignKey, Table
from sqlalchemy import String, Date
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

class Base(DeclarativeBase):
    pass

association_projects_tags = Table(
    "project_tags_link",
    Base.metadata,
    Column("project_id", ForeignKey("projects.id"), primary_key=True),
    Column("tag_id", ForeignKey("project_tags.id"), primary_key=True)
)

association_blogs_tags = Table(
    "blog_tags_link",
    Base.metadata,
    Column("blog_id", ForeignKey("blogs.id"), primary_key=True),
    Column("tag_id", ForeignKey("blog_tags.id"), primary_key=True)
)

class ProjectTag(Base):
    __tablename__ = "project_tags"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))

    projects: Mapped[List["Project"]] = relationship(
        secondary=association_projects_tags, back_populates="tags"
    )

class Project(Base):
    __tablename__ = "projects"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String())
    description: Mapped[str] = mapped_column(String())
    github: Mapped[str] = mapped_column(String(), nullable=True)
    itch: Mapped[str] = mapped_column(String(), nullable=True)
    weblink: Mapped[str] = mapped_column(String(), nullable=True)

    tags: Mapped[List[ProjectTag]] = relationship(
        secondary=association_projects_tags, back_populates="projects"
    )

    def __repr__(self) -> str:
        return f"Project: ID: {self.id}; name: {self.name}"

class BlogTag(Base):
    __tablename__ = "blog_tags"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))

    blogs: Mapped[List["Blog"]] = relationship(
        secondary=association_blogs_tags, back_populates="tags"
    )

class Blog(Base):
    __tablename__ = "blogs"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String())
    content: Mapped[str] = mapped_column(String())
    date: Mapped[datetime.date] = mapped_column(Date())

    tags: Mapped[List[BlogTag]] = relationship(
        secondary=association_blogs_tags, back_populates="blogs"
    )
