from pymongo import MongoClient

client = MongoClient()
db = client.my_vk_posts

# posts = main()

def insert_into_db(posts):
    if posts:
        result = db.my_vk_posts.insert_many([{
        'id': post.id,
        'date': str(post.date),
        'url' : post.url,
        'text': post.text,
        'likes': post.likes,
        'reposts': post.reposts} for post in posts
            if post and db.my_vk_posts.find({'id': post.id}).count() == 0])
        return result
    else:
        return 'Nothing to add to DB'
