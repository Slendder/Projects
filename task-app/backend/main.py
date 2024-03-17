from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def welcome():
    return {'message': 'Welcome to the API'}

@app.get('/api/task')
async def get_tasks():
    return {'all': 'hello'}

@app.post('/api/task')
async def get_tasks():
    return {'all': 'hello'}

@app.get('/api/task')
async def get_tasks():
    return {'all': 'hello'}

@app.get('/api/task')
async def get_tasks():
    return {'all': 'hello'}

@app.get('/api/task')
async def get_tasks():
    return {'all': 'hello'}
