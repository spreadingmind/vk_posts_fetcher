from pymongo import MongoClient
from post_downloader import main

client = MongoClient()
db = client.my_vk_posts

posts = main()

result = db.my_vk_posts.insert_many([{
    'id': post.id,
    'date': str(post.date),
    'url' : post.url,
    'text': post.text,
    'likes': post.likes,
    'reposts': post.reposts} for post in posts])

if len(result.inserted_ids) == len(posts):
    print ('Inserted properly')
