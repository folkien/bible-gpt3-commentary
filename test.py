import requests
from bs4 import BeautifulSoup
import openai


def post_to_facebook(comment, image_url):
    import facebook
    fb_access_token = 'your_facebook_access_token'
    page_id = 'your_facebook_page_id'
    graph = facebook.GraphAPI(access_token=fb_access_token, version='3.0')
    attachment = {
        'message': comment,
        'link': image_url,
    }
    graph.put_wall_post('', attachment=attachment, profile_id=page_id)


def main():
    ''' Pobiera czytanie z deon.pl'''
    #post_to_facebook(gpt4_comment, dalle2_image_url)


if __name__ == '__main__':
    main()
