import sqlite3
conn = sqlite3.connect('youtube_videos.db')
cursor = conn.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos (
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL
    )
''')

def list_videos():
    cursor.execute("SELECT * FROM videos")
    for rows in cursor.fetchall():
       print(rows)

def add_videos(name , time):
    cursor.execute("INSERT INTO videos (name,time) VALUES (?,?)", (name,time))
    conn.commit()

def update_videos(video_id,name,time):
    cursor.execute("UPDATE videos SET name= ?, time= ? WHERE id = ?",(video_id,name,time))
    conn.commit()

def delete_videos(video_id):
    
    cursor.execute("DELETE FROM videos where id=?",(video_id,))
    conn.commit()

def main():
  while True:
    print("\n YOUTUBE VIDEOS WITH DB")
    print("1. list all vidoes")
    print("2. add vidoes")
    print("3. update vidoes")
    print("4. delete vidoes")
    print("5. EXIT App")
    choice= input("enter your choice:")

    match choice:
          case '1':
              list_videos()
          case '2':
              name = input("enter the video name:")
              time = input("enter the lenght of video:")
              add_videos(name,time)
          case '3':
              video_id=input("enter the video id:")
              name = input("enter the video name:")
              time = input("enter the lenght of video:")
              update_videos(video_id,name,time)
          case '4':
              video_id=input("enter the video id:")
              
              delete_videos(video_id)
          case '5':
            break
          case '_':
            print("Invalid Choice")

  conn.close()

if __name__ == "__main__":
  main()
