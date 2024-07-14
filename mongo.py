from pymongo import MongoClient
from config import mongo, MongoURI
client = MongoClient(MongoURI)

#db = client[mongo["db"]]





# Replace the URI with your MongoDB URI
#client = MongoClient('mongodb://127.0.0.1:27019/')

# Replace 'myNewDatabase' with your database name
db = client['create_event']

# Replace 'myCollection' with your collection name
collection = db['new_events']

# Fetch all documents from the collection
#documents = collection.find()

class Mongo:

    def find_latest_reference_number():
        latest_document = collection.find().sort([('_id', -1)]).limit(1)

        # Print each document
        reference_number=[]
        for document in latest_document:
            print("111111111",document)
            reference_number.append(document["reference_number"])
        print("22222222222222222222",reference_number)
        return reference_number

    def find_event_db(categories):
        print("categoriessssssssssssssss", categories)
        result = collection.find({ "Data.event_category": { "$in": categories } })
        results=[]
        for event in result:
            #print("111111111",event)
            event["_id"] = str(event["_id"])  # Convert ObjectId to string
            results.append(event)
        print("full_catgorieeeesssssssssssss",results)
        return results

    # class Mongo:
    #     # Insert a single document into a database
    #       # Insert one or more document into a database
    def insert_one(data, coll_name):
        coll = db[coll_name]
        result = coll.insert_one(data)
        if result.acknowledged:
            # return result.acknowledged
            return result
        return None



