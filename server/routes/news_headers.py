from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from server.database import (
    retrieve_sporting_news_complete_headers,
    retrieve_political_news_complete_headers
)

from server.models.response import (
    successful_response_model,
    error_response_model
)

router = APIRouter()


@router.get("/politics", response_description="politics news headers from google news retrieved")
async def get_lmb_news_headers():
    politics_news_headers = await retrieve_political_news_complete_headers()
    if politics_news_headers:
        return successful_response_model(politics_news_headers, "mex politics news headers from google news retrieved successfully")
    return successful_response_model(politics_news_headers, "empty list returned")


@router.get("/sports", response_description="sports news headers with links from google news retrieved")
async def get_lmb_news_headers():
    sports_news_complete_headers = await retrieve_sporting_news_complete_headers()
    if sports_news_complete_headers:
        return successful_response_model(sports_news_complete_headers, "sports news headers with links from google news retrieved successfully")
    return successful_response_model(sports_news_complete_headers, "empty list returned")