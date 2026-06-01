#!/usr/bin/env python3
"""Return students sorted by average score."""

def top_students(mongo_collection):
"""Return all students sorted by average score."""
return mongo_collection.aggregate([
{"$addFields": {"averageScore": {"$avg": "$topics.score"}}},
{"$sort": {"averageScore": -1}},
])
