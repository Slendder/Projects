from motor.motor_asyncio import AsyncIOMotorClient
from models import Task

client = AsyncIOMotorClient('mongodb://localhost')
database = client.taskDataBase 
collection = database.tasks

async def get_one_task_id():
    return await collection.find_one({'_id': id})

async def get_all_task():
    tasks = []
    cursor = collection.find({})
    async for document in cursor:
        tasks.append(**document)
    return tasks

async def create_task(task):
    new_task = await collection.insert_one(task)
    created_task = await collection.find_one({'_id': new_task.inserted_id})
    return create_task

async def update_task(id: str, task):
    await collection.update_one({'_id': id}, {'$set': task})
    document = await collection.find_one({'_id': id})
    return document


async def delete_task(id: str):
    await collection.delete_one({'_id': id})
    return True