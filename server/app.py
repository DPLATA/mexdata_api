from fastapi import FastAPI, APIRouter, Body
from fastapi.encoders import jsonable_encoder
from server.routes.lmb import router as lmb_router

app = FastAPI()

# test motor vs pymongo
app.include_router(lmb_router, tags=["lmb"], prefix="/lmb")

@app.get("/")
async def root():
    return {"message": "Hello World"}