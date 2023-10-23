#!/usr/bin/env python3
"""
Module to fetch documents from a collection.
"""
import pymongo

def list_all(mongo_collection):
    """
    Lists all documents from a given collection.
    
    Args:
        - mongo_collection: the pymongo collection object.
        
    Returns:
        - List of documents.
    """
    if mongo_collection is None:
        return []
    return [doc for doc in mongo_collection.find()]
