from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from server.database import (
    retrieve_geojson_all_feature_collections,
    retrieve_geojson_all_single_features
)

from server.models.response import (
    successful_response_model,
    error_response_model
)

router = APIRouter()


@router.get("/single_features", response_description="geoJson single features retrieved")
async def get_geojson_mex_map_as_single_features():
    mex_geojson_single_features = await retrieve_geojson_all_single_features()
    if mex_geojson_single_features:
        return successful_response_model(mex_geojson_single_features, "geoJson single features retrieved successfully")
    return successful_response_model(mex_geojson_single_features, "empty list returned")


@router.get("/feature_collections", response_description="geoJson feature collections retrieved")
async def get_geojson_mex_map_as_feature_collection():
    mex_geojson_feature_collections = await retrieve_geojson_all_feature_collections()
    if mex_geojson_feature_collections:
        return successful_response_model(mex_geojson_feature_collections, "geoJson feature collections retrieved successfully")
    return successful_response_model(mex_geojson_feature_collections, "empty list returned")