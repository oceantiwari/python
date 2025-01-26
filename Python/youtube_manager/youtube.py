import json

def load_data():
  try:
    with open('youtube.txt','r') as file:
      return json.load(file)
  except FileNotFoundError:
    return []

def save_data_helper(video):
  with open('youtube.txt','w') as file:
    json.dump(video,file)

def list_all_videos(video):
  print("\n")
  print("*" * 70)

  for index,video in enumerate(video,start=1):
    print(f"{index}.{video['name']},Duration:{video['time']} ")
  
  print("\n")
  print("*" * 70)

def add_videos(video):
  name=input("enter the video title:")
  time=input("enter the timing:")
  video.append({'name':name,'time':time})
  save_data_helper(video)

def update_videos(video):
  list_all_videos(video)
  index = int(input("Enter the video number to update"))
  if 1 <= index <= len(video):
      name = input("Enter the new video name")
      time = input("Enter the new video time")
      video[index-1] = {'name':name, 'time': time}
      save_data_helper(video)
  else:
      print("Invalid index selected")

def delete_videos(video):
  list_all_videos(video)
  index = int(input("Enter the video number to be deleted"))
  
  if 1<= index <= len(video):
      del video[index-1]
      save_data_helper(video)
  else:
      print("Invalid video index selected")


def main():
    video = load_data()
    while True:
        print("Youtube Manager App  | choose an app")
        print("1. list all videos")
        print("2.Add a youtube video")
        print("3. Update a youtube video details")
        print("4. Delete a Youtbe video")
        print("5. Exit")
        choice = input("enter your choice:")

        match choice:
          case '1':
              list_all_videos(video)
          case '2':
              add_videos(video)
          case '3':
              update_videos(video)
          case '4':
              delete_videos(video)
          case '5':
              print("Exiting the application.")
              break
          case _:
              print("Invalid choice. Please try again.")


if __name__== "__main__":
  main()