from os.path import join, dirname
import os
import pytz
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


mongo = {
    "host": os.getenv('mongo_host'),
    "port": os.getenv('mongo_port'),
    "db": os.getenv('mongo_db'),
    "user": os.getenv('mongo_user'),
    "pass": os.getenv('mongo_pwd')
}

print("mongomongomongomongo",mongo)

auth = "{}:{}".format(mongo['user'], mongo['pass'])
link = "{}:{}/{}".format(mongo['host'], mongo['port'], mongo['db'])
MongoURI = "mongodb://{}".format(link)


base_path = "./data/"
MAX_TIME_MS = 1000