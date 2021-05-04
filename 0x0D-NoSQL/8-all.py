#!/usr/bin/env python3
"""
List all documents in Python
"""
import pymongo


def list_all(mongo_collection):
    """
    function that lists all documents in a [mongo] collection
    """
    docs = mongo_collection.find()
    return [doc for doc in docs]