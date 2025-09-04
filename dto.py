from typing import List
from pydantic import BaseModel
import datetime

class ProjectTagResponse(BaseModel):
    id: int
    name: str

class ProjectResponse(BaseModel):
    id: int
    name: str
    description: str
    github: str | None
    itch: str | None
    weblink: str | None
    tags: List[ProjectTagResponse]

class BlogTagResponse(BaseModel):
    id: int
    name: str

class BlogResponse(BaseModel):
    id: int
    name: str
    content: str
    date: datetime.date
    tags: List[BlogTagResponse]