from pymongo import MongoClient
import time

client = MongoClient('mongodb://localhost:27017')

db = client['my_app']

collection = db['numbers']

query = {"num": {"$gt": 180000}}


start_time = time.time()
result = collection.find(query)
end_time = time.time()

execution_time = end_time - start_time


print("Query execution time: {:.9f} seconds".format(execution_time))
