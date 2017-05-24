class VKApiError(RuntimeError):
    pass

class Post:

    def __init__(self, id, likes, reposts, date, text, url=None):
        self.id = id
        self.likes = likes
        self.reposts = reposts
        self.text = text
        self.date = date
        self.url = url

    def pretty_post(self):
        data = {'id': self.id, 'date': self.date , 'url': self.url,
                'likes': self.likes, 'reposts': self.reposts,
                'text': self.text}

        pretty_format = '\nDate: {d[date]} \nID: {d[id]} \nPost URL: {d[url]} \n' \
                        'Text: {d[text]} \nLikes: {d[likes]}  \nReposts: {d[reposts]}\n'.format(d=data)

        return pretty_format