import motor.motor_asyncio as motor
from decouple import config

MONGO_URI = config('MONGO_URI')
client = motor.AsyncIOMotorClient(MONGO_URI)
db = client[config('MONGO_DB')]
player_hitting_collection = db.get_collection(config('MONGO_PLAYER_HITTING_COLLECTION'))
team_hitting_collection = db.get_collection(config('MONGO_TEAM_HITTING_COLLECTION'))
team_pitching_collection = db.get_collection(config('MONGO_TEAM_PITCHING_COLLECTION'))

single_features_collection = db.get_collection(config('MONGO_MEX_MAP_SINGLE_FEATURES_COLLECTION'))
feature_collection_collection = db.get_collection(config('MONGO_MEX_MAP_FEATURE_COLLECTION_COLLECTION'))

sports_news_headers_complete_collection = db.get_collection(config('MONGO_MEX_SPORTING_NEWS_COMPLETE_COLLECTION'))
politics_news_headers_complete_collection = db.get_collection(config('MONGO_MEX_POLITICAL_NEWS_COMPLETE_COLLECTION'))


# helpers
def player_occurrence_helper(occurrence) -> dict:
    return {
        "id": str(occurrence["_id"]),
        "player": occurrence["player"],
        "team": occurrence["team"],
        "G": occurrence["G"],
        "AB": occurrence["AB"],
        "R": occurrence["R"],
        "H": occurrence["H"],
        "2B": occurrence["2B"],
        "3B": occurrence["3B"],
        "HR": occurrence["HR"],
        "RBI": occurrence["RBI"],
        "BB": occurrence["BB"],
        "SO": occurrence["SO"],
        "SB": occurrence["SB"],
        "CS": occurrence["CS"],
        "AVG": occurrence["AVG"],
        "OBP": occurrence["OBP"],
        "SLG": occurrence["SLG"],
        "OPS": occurrence["OPS"]
    }


def team_hitting_stat_occurrence_helper(occurrence) -> dict:
    return {
        "id": str(occurrence["_id"]),
        "team": occurrence["team"],
        "league": occurrence["league"],
        "G": occurrence["G"],
        "AB": occurrence["AB"],
        "R": occurrence["R"],
        "H": occurrence["H"],
        "2B": occurrence["2B"],
        "3B": occurrence["3B"],
        "HR": occurrence["HR"],
        "RBI": occurrence["RBI"],
        "BB": occurrence["BB"],
        "SO": occurrence["SO"],
        "SB": occurrence["SB"],
        "CS": occurrence["CS"],
        "AVG": occurrence["AVG"],
        "OBP": occurrence["OBP"],
        "SLG": occurrence["SLG"],
        "OPS": occurrence["OPS"]
    }


def team_pitching_stat_occurrence_helper(occurrence) -> dict:
    return {
        "id": str(occurrence["_id"]),
        "team": occurrence["team"],
        "league": occurrence["league"],
        "W": occurrence["W"],
        "L": occurrence["L"],
        "ERA": occurrence["ERA"],
        "G": occurrence["G"],
        "GS": occurrence["GS"],
        "CG": occurrence["CG"],
        "SHO": occurrence["SHO"],
        "SV": occurrence["SV"],
        "SVO": occurrence["SVO"],
        "IP": occurrence["IP"],
        "H": occurrence["H"],
        "R": occurrence["R"],
        "ER": occurrence["ER"],
        "HR": occurrence["HR"],
        "HB": occurrence["HB"],
        "BB": occurrence["BB"],
        "SO": occurrence["SO"],
        "WHIP": occurrence["WHIP"],
        "AVG": occurrence["AVG"]
    }

def single_features_occurrence_helper(occurrence) -> dict:
    return {
        "id": str(occurrence["_id"]),
        "type": occurrence["type"],
        "properties": occurrence["properties"],
        "geometry": occurrence["geometry"]
    }


def feature_collection_occurrence_helper(occurrence) -> dict:
    return {
        "id": str(occurrence["_id"]),
        "type": occurrence["type"],
        "features": occurrence["features"]
    }


def news_header_complete_occurrence_helper(occurrence) -> dict:
    return {
        "id": str(occurrence["_id"]),
        "title": occurrence["title"],
        "link": occurrence["link"],
        "tag": occurrence["tag"]
    }


# Retrieve hitting stats for all players present in the database
async def retrieve_players_hitting_stats():
    players = []
    async for player in player_hitting_collection.find():
        players.append(player_occurrence_helper(player))
    return players


# Retrieve hitting stats for all teams present in the database
async def retrieve_teams_hitting_stats():
    teams = []
    async for team in team_hitting_collection.find():
        teams.append(team_hitting_stat_occurrence_helper(team))
    return teams


# Retrieve pitching stats for all teams present in the database
async def retrieve_teams_pitching_stats():
    teams = []
    async for team in team_pitching_collection.find():
        teams.append(team_pitching_stat_occurrence_helper(team))
    return teams


# Retrieve all geoJson single features present in the database
async def retrieve_geojson_all_single_features():
    geojson_single_features = []
    async for feature in single_features_collection.find():
        geojson_single_features.append(single_features_occurrence_helper(feature))
    return geojson_single_features


# Retrieve all geoJson feature collections present in the database
async def retrieve_geojson_all_feature_collections():
    geojson_feature_collections = []
    async for feature_collection in feature_collection_collection.find():
        geojson_feature_collections.append(feature_collection_occurrence_helper(feature_collection))
    return geojson_feature_collections

# Retrieve all geoJson feature collections present in the database
async def retrieve_sporting_news_complete_headers():
    news_headers = []
    async for header in sports_news_headers_complete_collection.find():
        news_headers.append(news_header_complete_occurrence_helper(header))
    return news_headers


# Retrieve all geoJson feature collections present in the database
async def retrieve_political_news_complete_headers():
    news_headers = []
    async for header in politics_news_headers_complete_collection.find():
        news_headers.append(news_header_complete_occurrence_helper(header))
    return news_headers
