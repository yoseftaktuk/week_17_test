from pymongo import MongoClient
import os
import utilis
uri = os.getenv('URI',"mongodb://mongo:27017/")
class Mongo_manager:
    def __init__(self):
        self.cliet =  MongoClient(uri)
        self.cliet['admin']
        self.db = self.cliet['admin']
        self.collection = self.db['registrs']
        self.collection.insert_many(utilis.save_file())
    def inser_register(self, data):
        if isinstance(data, dict):
            self.collection.insert_one(data)
            return {'massage':'data save'}
        self.collection.insert_many(data)
    def get_30(self, num):
        return self.collection.find({}, {'_id':0}).limit(num).skip(num + 30).to_list()
    
    