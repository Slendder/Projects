from fastapi import FastAPI
from database import get_all_task, create_task
from models import Task
app = FastAPI()

@app.get('/')

def welcome():
    return {'message': 'Welcome!'}

@app.get('/api/tasks')
async def get_task():
    tasks = await get_all_task()
    return tasks

@app.post('/api/tasks')
async def save_task(task: Task):
    response = await create_task(task.dict())
    print(response)
    return 'saving task'

@app.get(f'/api/tasks/{id}')
async def get_single_task():
    return "single task?"

@app.put(f'/api/tasks/{id}')
async def update_task():
    return "updating task?"

@app.delete(f'/api/tasks/{id}')
async def delete_task():
    return "delete task?"
