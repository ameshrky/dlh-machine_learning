#!/usr/bin/env python3
"""Provide statistics about Nginx logs stored in MongoDB."""
from pymongo import MongoClient

if name == "main":
collection = MongoClient("mongodb://127.0.0.1:27017").logs.nginx
methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

print("{} logs".format(collection.count_documents({})))
print("Methods:")
for method in methods:
    print("\tmethod {}: {}".format(
        method, collection.count_documents({"method": method})))
print("{} status check".format(
    collection.count_documents({"method": "GET", "path": "/status"})))

