import motor.motor_asyncio as motor
from decouple import config

MONGO_URI = config('MONGO_URI')
client = motor.AsyncIOMotorClient(MONGO_URI)
db = client[config('MONGO_DB')]
collection = db.get_collection(config('MONGO_HITTING_COLLECTION'))

# helpers
def ocurrence_helper(ocurrence) -> dict:
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

# Retrieve all players present in the database
async def retrieve_players_hitting_stats():
    players = []
    async for player in collection.find():
        players.append(ocurrence_helper(player))
    return players
