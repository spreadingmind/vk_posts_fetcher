from pymongo import MongoClient
from post_downloader import main

client = MongoClient()
db = client.my_vk_posts

# posts = main()

def insert_into_db(posts):
    result = db.my_vk_posts.insert_many([{
        'id': post.id,
        'date': str(post.date),
        'url' : post.url,
        'text': post.text,  
        'likes': post.likes,
        'reposts': post.reposts} for post in posts])
    return result

# if len(result.inserted_ids) == len(posts):
#     print ('Inserted properly')
