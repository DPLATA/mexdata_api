import motor.motor_asyncio as motor
from decouple import config

MONGO_URI = config('MONGO_URI')
client = motor.AsyncIOMotorClient(MONGO_URI)
db = client[config('MONGO_DB')]
player_hitting_collection = db.get_collection(config('MONGO_PLAYER_HITTING_COLLECTION'))
team_hitting_collection = db.get_collection(config('MONGO_TEAM_HITTING_COLLECTION'))

feature_collection = db.get_collection(config('MONGO_TEAM_MEX_MAP_FEATURE_COLLECTION'))


# helpers
def player_ocurrence_helper(ocurrence) -> dict:
    return {
        "id": str(ocurrence["_id"]),
        "player": ocurrence["player"],
        "team": ocurrence["team"],
        "G": ocurrence["G"],
        "AB": ocurrence["AB"],
        "R": ocurrence["R"],
        "H": ocurrence["H"],
        "2B": ocurrence["2B"],
        "3B": ocurrence["3B"],
        "HR": ocurrence["HR"],
        "RBI": ocurrence["RBI"],
        "BB": ocurrence["BB"],
        "SO": ocurrence["SO"],
        "SB": ocurrence["SB"],
        "CS": ocurrence["CS"],
        "AVG": ocurrence["AVG"],
        "OBP": ocurrence["OBP"],
        "SLG": ocurrence["SLG"],
        "OPS": ocurrence["OPS"]
    }


def team_ocurrence_helper(ocurrence) -> dict:
    return {
        "id": str(ocurrence["_id"]),
        "team": ocurrence["team"],
        "league": ocurrence["league"],
        "G": ocurrence["G"],
        "AB": ocurrence["AB"],
        "R": ocurrence["R"],
        "H": ocurrence["H"],
        "2B": ocurrence["2B"],
        "3B": ocurrence["3B"],
        "HR": ocurrence["HR"],
        "RBI": ocurrence["RBI"],
        "BB": ocurrence["BB"],
        "SO": ocurrence["SO"],
        "SB": ocurrence["SB"],
        "CS": ocurrence["CS"],
        "AVG": ocurrence["AVG"],
        "OBP": ocurrence["OBP"],
        "SLG": ocurrence["SLG"],
        "OPS": ocurrence["OPS"]
    }


def feature_ocurrence_helper(ocurrence) -> dict:
    return {
        "id": str(ocurrence["_id"]),
        "type": ocurrence["type"],
        "properties": ocurrence["properties"],
        "geometry": ocurrence["geometry"]
    }


# Retrieve all players hitting stats present in the database
async def retrieve_players_hitting_stats():
    players = []
    async for player in player_hitting_collection.find():
        players.append(player_ocurrence_helper(player))
    return players


# Retrieve all teams hitting stats present in the database
async def retrieve_teams_hitting_stats():
    teams = []
    async for team in team_hitting_collection.find():
        teams.append(team_ocurrence_helper(team))
    return teams


# Retrieve all geoJson features present in the database
async def retrieve_geojson_feature():
    geojson_features = []
    async for feature in feature_collection.find():
        geojson_features.append(feature_ocurrence_helper(feature))
    return geojson_features
