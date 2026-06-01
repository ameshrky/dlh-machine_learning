#!/usr/bin/env python3
"""Print Nginx log statistics stored in MongoDB."""
from pymongo import MongoClient


if __name__ == "__main__":
    collection = MongoClient("mongodb://127.0.0.1:27017").logs.nginx
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    print("{} logs".format(collection.count_documents({})))
    print("Methods:")
    for method in methods:
        print("\tmethod {}: {}".format(method, collection.count_documents({"method": method})))
    print("{} status check".format(collection.count_documents({"method": "GET", "path": "/status"})))
    print("IPs:")
    for doc in collection.aggregate([{"$group": {"_id": "$ip", "count": {"$sum": 1}}}, {"$sort": {"count": -1}}, {"$limit": 10}]):
        print("\t{}: {}".format(doc["_id"], doc["count"]))
