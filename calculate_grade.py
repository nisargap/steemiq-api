from utils import cleanhtml, cleanmarkdown
from textstat.textstat import textstat
import get_posts

NUM_POSTS = 100

def calc_iq(average):
  if(average > 10):
    return int(((140 + average) % 20) + 122)
  if(average < 10):
    return int(((100 + average) % 10) + 90)

def calculate_grade(blog):
  grades = []
  summation = 0
  count = len(blog)
  # accounting for the case in which the blog is 0 length
  if(count == 0):
    count += 1
  for post in blog:
    if 'comment' in post:
      if 'body' in post['comment']:
        raw = post['comment']['body']
        current = cleanhtml(cleanmarkdown(raw))
        if(len(current) < 10):
          continue
        else:
          grade = textstat.flesch_kincaid_grade(current)
          summation += grade
          grades.append({ "title" : post["comment"]["title"], "grade" : grade })
  return {"grades": grades, "average": summation/count, "iq":  calc_iq(summation/count)}

def calculate_user(username):
  response = get_posts.retrieve_blog(username, 0, 100)
  if(response["status"] == True):
    response = calculate_grade(response["payload"])
    return { "status" : True, "payload": response }
  else:
    return { "status" : False, "payload": response["message"] }
'''

Example Usage:

response = get_posts.retrieve_blog("nphacker", 0, 500)
response = calculate_grade(response["payload"])

'''
