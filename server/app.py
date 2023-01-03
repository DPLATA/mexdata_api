from fastapi import FastAPI, APIRouter, Body
# from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
from server.routes.lmb import router as lmb_router

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# test motor vs pymongo
app.include_router(lmb_router, tags=["lmb"], prefix="/lmb")

@app.get("/")
async def root():
    return {"message": "Hello World"}