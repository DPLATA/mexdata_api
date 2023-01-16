from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from server.database import (
    retrieve_players_hitting_stats,
    retrieve_teams_hitting_stats,
    retrieve_teams_pitching_stats,
    retrieve_lmb_news_headers,
    retrieve_lmb_news_complete_headers
)

from server.models.response import (
    successful_response_model,
    error_response_model
)

router = APIRouter()


@router.get("/players_hitting", response_description="hitting stats for players retrieved")
async def get_players_hitting_stats():
    players_hitting_stats = await retrieve_players_hitting_stats()
    if players_hitting_stats:
        return successful_response_model(players_hitting_stats, "players hitting stats retrieved successfully")
    return successful_response_model(players_hitting_stats, "empty list returned")


@router.get("/teams_hitting", response_description="hitting stats for teams retrieved")
async def get_teams_hitting_stats():
    teams_hitting_stats = await retrieve_teams_hitting_stats()
    if teams_hitting_stats:
        return successful_response_model(teams_hitting_stats, "teams hitting stats retrieved successfully")
    return successful_response_model(teams_hitting_stats, "empty list returned")


@router.get("/teams_pitching", response_description="pitching stats for teams retrieved")
async def get_teams_pitching_stats():
    teams_pitching_stats = await retrieve_teams_pitching_stats()
    if teams_pitching_stats:
        return successful_response_model(teams_pitching_stats, "teams pitching stats retrieved successfully")
    return successful_response_model(teams_pitching_stats, "empty list returned")


@router.get("/news_headers", response_description="lmb news headers from google news retrieved")
async def get_lmb_news_headers():
    lmb_news_headers = await retrieve_lmb_news_headers()
    if lmb_news_headers:
        return successful_response_model(lmb_news_headers, "lmb news headers from google news retrieved successfully")
    return successful_response_model(lmb_news_headers, "empty list returned")


@router.get("/news_complete_headers", response_description="lmb news headers with links from google news retrieved")
async def get_lmb_news_headers():
    lmb_news_complete_headers = await retrieve_lmb_news_complete_headers()
    if lmb_news_complete_headers:
        return successful_response_model(lmb_news_complete_headers, "lmb news headers with links from google news retrieved successfully")
    return successful_response_model(lmb_news_complete_headers, "empty list returned")