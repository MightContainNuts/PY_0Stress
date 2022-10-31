import dependencies, requests

CLIENT_ID = "94978"
CLIENT_SECRET = "ee844c68acdd40e1c6b59a7734479e04a2a09c30"
REDIRECT_URI = "http://localhost:65010/reddit_callback"

https://www.strava.com/oauth/authorize?client_id=94978&redirect_uri=http://localhost&response_type=code&scope=activity:read_all
http://localhost/?state=&code=c853bdc6810583912f1c82a18b0c83a4f2803e40&scope=read,activity:read_all

c853bdc6810583912f1c82a18b0c83a4f2803e40


POST
https://www.strava.com/oauth/token?client_id=94978&client_secret=ee844c68acdd40e1c6b59a7734479e04a2a09c30&code=c853bdc6810583912f1c82a18b0c83a4f2803e40&grant_type=authorization_code