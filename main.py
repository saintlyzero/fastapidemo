from fastapi import FastAPI

from model import Events
from utils import Utils

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello":"World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


@app.post("/event/")
async def add_entry(events: Events):
    db_details = {
        'drivername': 'postgres',
        'username': 'postgres',
        'password': 'admin',
        'host': '127.0.0.1',
        'port': 5432,
        'database':'demo'
    }
    url = Utils.create_connection(db_details)
    Utils.test_sqlalchemy_core(url, n=1000)
    return events
