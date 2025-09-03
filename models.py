import datetime
from sqlalchemy import ForeignKey
from sqlalchemy import String, Date
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

class Base(DeclarativeBase):
    pass

class Project(Base):
    __tablename__ = "projects"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String())
    description: Mapped[str] = mapped_column(String())

    def __repr__(self) -> str:
        return f"Project: ID: {self.id}; name: {self.name}"

class Blog(Base):
    __tablename__ = "blogs"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String())
    content: Mapped[str] = mapped_column(String())
    date: Mapped[datetime.date] = mapped_column(Date())
