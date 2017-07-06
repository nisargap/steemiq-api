from steem import Steem

# Retrieves a steemit blog given a valid username
def retrieve_blog(username, entry, num_posts):
  if(len(username) == 0):
    return { "status" : False, "message" : "Please enter a valid username", "payload": [] }
  steem = Steem()
  username = username.replace("@", "")
  blog = steem.get_blog(username, entry, num_posts)
  if(len(blog) == 0):
    return { "status" : False, "message" : "Could not retrieve user blog", "payload": [] }
  else:
    return { "status" : True, "payload" : blog }
