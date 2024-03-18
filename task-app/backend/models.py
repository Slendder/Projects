from pydantic import BaseModel

class Task(BaseModel):
    id
    title: str
    description: str
    completed: bool = False
       