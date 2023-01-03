from fastapi import FastAPI, APIRouter, Body
from fastapi.encoders import jsonable_encoder
from server.database import retrieve_players_hitting_stats


app = FastAPI()

# test motor vs pymongo

def ResponseModel(data, message):
    return {
        "data": data,
        "code": 200,
        "message": message,
    }

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.get("/players", response_description="players retrieved")
async def get_players_hitting_stats():
    hitting_stats = await retrieve_players_hitting_stats()
    if hitting_stats:
        return ResponseModel(hitting_stats, "Players data retrieved successfully")
    return ResponseModel(hitting_stats, "Empty list returned")
