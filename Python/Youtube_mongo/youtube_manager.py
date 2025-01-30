from pymongo import MongoClient
from bson import ObjectId

client = MongoClient("mongodb+srv://youtubepy:youtubepy@youtube.l0yts.mongodb.net/")

db = client["ytmanager"]
video_collection =db["videos"]

print(video_collection)

def list_videos():
    for video in video_collection.find():
        print(f"Video_id:{video['_id']}, Name:{video['name']} and Time : {video['time']}")

def add_videos(name,time):
    video_collection.insert_one({"name":name , "time": time})

def update_videos(video_id,name,time):
    video_collection.update_one(
        {'_id' :ObjectId(video_id)},
        {"_set":{"name":name , "time": time}}
    )

def delete_video(video_id):
    video_collection.delete_one({"_id":ObjectId(video_id)})

    

def main():
  while True:
    print("\n Youtube Manager app")
    print("1. list all videos ")
    print("2. add a new video")
    print("3. update the video")
    print("4. delete the video")
    print("5. exit  the application")
    choice=input("enter the choice: ")

    match choice:
          case '1':
              list_videos()
          case '2':
              name=input("enter the video name:")
              time=input("enter the video time:")
              add_videos(name,time)
          case '3':
              video_id=input("enter the video id :")
              name=input("enter the video name:")
              time=input("enter the video time:")
              update_videos(video_id,name,time)
          case '4':
              video_id= input("enter the video id to be deleted:")
              delete_video(video_id)
          case '5':
              print("Exiting the application.")
              break
          case _:
              print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
 
