from pymongo import MongoClient

client = MongoClient()
db = client.my_vk_posts

# posts = main()

def insert_into_db(posts):
    for post in posts:
        db.my_vk_posts.update_one({'id': post.id}, {'$set': {
        'id': post.id,
        'date': str(post.date),
        'url' : post.url,
        'text': post.text,
        'likes': post.likes,
        'reposts': post.reposts}}, upsert=True)

