from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from server.database import (
    retrieve_geojson_feature
)

from server.models.response import (
    successful_response_model,
    error_response_model
)

router = APIRouter()


@router.get("/features", response_description="geoJson features retrieved")
async def get_geojson_mex_map():
    mex_geojson_feature_collection = await retrieve_geojson_feature()
    if mex_geojson_feature_collection:
        return successful_response_model(mex_geojson_feature_collection, "geoJson features retrieved successfully")
    return successful_response_model(mex_geojson_feature_collection, "empty list returned")