import motor
from config import MONGO_HOST,MONGO_PORT


def make_mongo():
    try:
        client = motor.MotorClient(MONGO_HOST, MONGO_PORT, connectTimeoutMS=2000)
        db = client["xxx"]
    except Exception as e:
        db = ""
        print e, "mongo"
    return db
