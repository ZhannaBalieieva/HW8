from mongoengine import connect
import configparser
from pymongo import MongoClient
from pymongo.server_api import ServerApi

config = configparser.ConfigParser()
config.read('config.ini')

mongo_user = config.get('DB', 'user')
mongodb_pass = config.get('DB', 'pass')
db_name = config.get('DB', 'db_name')
domain = config.get('DB', 'domain')

# connect to cluster on AtlasDB with connection string
#######connect(host="mongodb://127.0.0.1:27017/my_db")##########
connect(host=f"""mongodb+srv://{mongo_user}:{mongodb_pass}@{domain}/{db_name}?retryWrites=true&w=majority""", ssl=True)




