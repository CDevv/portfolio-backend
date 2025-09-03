import service
import dto
from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/projects", response_model=list[dto.ProjectResponse])
async def get_projects():
    return service.get_all_projects()

@app.get("/projects/", response_model=dto.ProjectResponse)
async def get_project(id: int = 1):
    res = service.get_project_by_id(id)
    if res is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return res

@app.get("/blogs", response_model=list[dto.BlogResponse])
async def get_blogs():
    return service.get_all_blogs()

@app.get("/blogs/", response_model=dto.BlogResponse)
async def get_blog(id: int = 1):
    res = service.get_blog_by_id(id)
    if res is None:
        raise HTTPException(status_code=404, detail="Blog not found")
    return res