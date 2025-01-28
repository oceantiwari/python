from pymongo import MongoClient

client = MongoClient("mongodb+srv://youtubepy:youtubepy@youtube.l0yts.mongodb.net/youtubeDB")

db = client["ytmanager"]
video_collection =db["videos"]

print(video_collection)