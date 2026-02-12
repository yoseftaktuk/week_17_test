from pymongo import MongoClient
db_username = ''
db_password = ''
hostname = 'localhost'
port = 27017
uri = "mongodb://mongo:27017/"
class Mongo_manager:
    def __init__(self):
        #self.cliet =  MongoClient(f"mongodb://{db_username}:{db_password}@{hostname}:{port}")
        self.cliet =  MongoClient(uri)
        self.cliet['admin']
        self.db = self.cliet['admin']
        self.collection = self.db['registrs']
    def inser_register(self, data):
        if isinstance(data, dict):
            self.collection.insert_one(data)
            return {'massage':'data save'}
        self.collection.insert_many(data)
    def get_30(self, num):
        return self.collection.find().skip(num).to_list() 
    
    