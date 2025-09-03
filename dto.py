from pydantic import BaseModel
import datetime

class ProjectResponse(BaseModel):
    id: int
    name: str
    description: str

class BlogResponse(BaseModel):
    id: int
    name: str
    content: str
    date: datetime.date