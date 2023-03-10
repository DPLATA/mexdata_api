from fastapi import FastAPI, APIRouter, Body
# from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
from server.routes.lmb import router as lmb_router
from server.routes.mex_map import router as mex_map_router
from server.routes.news_headers import router as news_router

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
app.include_router(news_router, tags=["news_headers"], prefix="/news")
app.include_router(mex_map_router, tags=["mex_map"], prefix="/mex_map")

@app.get("/")
async def root():
    return {"message": "Hello World"}