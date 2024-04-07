from pymongo import MongoClient
import time

client = MongoClient('mongodb://localhost:27017')

db = client['my_app']

collection = db['courses']

query = {"student_surname": "Smith"}
sort_criteria = [("subject", 1), ("grade", -1)]

start_time = time.time()
result = collection.find(query).sort(sort_criteria)
end_time = time.time()

execution_time = end_time - start_time

for doc in result:
    print(doc)

print("Query execution time: {:.6f} seconds".format(execution_time))
