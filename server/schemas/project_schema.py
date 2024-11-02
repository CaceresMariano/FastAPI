from datetime import datetime

from pydantic import BaseModel


class NewProjectRequest(BaseModel):
    title: str
    status: str = 'new'
    description: str = ''

class ProjectRequest(BaseModel):
    title: str | None = None
    status: str | None = None
    description: str | None = None 

class ProjectResponse(BaseModel):
    id: int
    title: str
    status: str = 'new'
    description: str = ''
    create_at: datetime
    update_at: datetime
