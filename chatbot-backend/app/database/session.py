from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

db = client["ai_chatbot"]

chat_collection = db["chat_history"]