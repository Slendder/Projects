from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def welcome():
    return {'message': 'Welcome!'}

@app.get('/api/tasks')
async def get_task():
    return "something?"

@app.post('/api/tasks')
async def create_task():
    return "create task?"

@app.get(f'/api/tasks/{id}')
async def get_single_task():
    return "single task?"

@app.put(f'/api/tasks/{id}')
async def update_task():
    return "updating task?"

@app.delete(f'/api/tasks/{id}')
async def delete_task():
    return "delete task?"
