from __future__ import print_function  #for python2
import requests
import datetime
from constants import VKAPI_URL, VKAPI_VERSION
from utils import VKApiError, Post as Post
from settings import my_user_id as my_page_id, access_token as access_token
import post_db

class PostDownloader:

    def __init__(self, page_id):
        self.page_id = page_id
        self.api_url = VKAPI_URL
        self.request_params = {'owner_id': self.page_id,  'v': VKAPI_VERSION,
                               'access_token': access_token}

    def _number_of_posts(self):
        """ Returns total number of post on the page """
        self.request_params['offset'] = 0
        self.request_params['count'] = 1
        url = self.api_url + 'wall.get'

        response = requests.get(url, params=self.request_params).json()

        if 'error' in response:
            raise VKApiError(response['error']['error_msg'])
        return response['response']['count']

    def fetch(self, init_offset=0, num_to_fetch=None):
        """ Downloads 'num_to_fetch' posts starting from 'init_offset' position """

        num_to_fetch = num_to_fetch or self._number_of_posts()
        self.request_params['offset'] = init_offset
        self.request_params['count'] = min(num_to_fetch, 100)
        fetched_posts = []
        fetched_counter = 0

        while fetched_counter != num_to_fetch:

            url = self.api_url + 'execute.getPosts?' #see details @ https://vk.com/dev/execute
            response = requests.get(url, params=self.request_params).json()

            if 'error' in response:
                raise VKApiError(response['error']['error_msg'])

            posts = response['response']
            fetched_counter += len(posts)
            received_data = response['response']

            for chunk in received_data:
                for post in chunk:
                    post = Post(
                        id=post['id'],
                        text=post['text'],
                        likes=post['likes']['count'],
                        reposts=post['reposts']['count'],
                        date=datetime.date.fromtimestamp(post['date']),
                        url='https://vk.com/wall{0}_{1}'.format(self.page_id, post['id'])
                    )
                    fetched_posts.append(post)

            self.request_params['offset'] += 100
            self.request_params['count'] = min(num_to_fetch - fetched_counter, 100)

            return fetched_posts

def main():
    downloader = PostDownloader(page_id=my_page_id)
    posts = downloader.fetch()
    return post_db.insert_into_db(posts)

if __name__ == '__main__':
    main()