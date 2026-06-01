#!/usr/bin/env python3
"""Find schools by topic."""


def schools_by_topic(mongo_collection, topic):
    """Return schools having a specific topic."""
    return mongo_collection.find({"topics": topic})
