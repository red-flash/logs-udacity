# "Database code" for the DB Forum.

import datetime
import psycopg2
import bleach

DBNAME = "forum"



POSTS = [("This is the first post.", datetime.datetime.now())]

def get_posts():
  db = psycopg2.connect(database=DBNAME)
  cursor = db.cursor()
  cursor.execute("select content,time from posts order by time desc;")
  results = cursor.fetchall()
  db.close()
  return results
  
  

def add_post(content):
  db = psycopg2.connect(database=DBNAME)
  cursor = db.cursor()
  #how does this C syntax insert the variable into the insert statement?
  cursor.execute("insert into posts values (%s)",(bleach.clean(content),))
  cursor.execute("update posts set content = 'begone!!' where content like '%script%'")
  cursor.execute("delete from posts where content='begone!!'")
  db.commit()
  db.close()
  


