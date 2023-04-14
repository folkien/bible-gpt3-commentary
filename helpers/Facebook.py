import facebook
import os

import requests

# Get facebook access token from env
fb_access_token = os.environ.get('FB_ACCESS_TOKEN', None)
if (fb_access_token is None):
    raise ValueError('Facebook access token not found in env.')

# Get facebook page id from env
fb_page_id = os.environ.get('FB_PAGE_ID', None)
if (fb_page_id is None):
    raise ValueError('Facebook page id not found in env.')

# Get facebook app id from env
app_id = os.environ.get('FB_APP_ID', None)
if (app_id is None):
    raise ValueError('Facebook app id not found in env.')

# Get facebook app secret from env
app_secret = os.environ.get('FB_APP_SECRET', None)
if (app_secret is None):
    raise ValueError('Facebook app secret not found in env.')


def fb_get_longlive_access_token():
    # Parametry żądania
    params = {
        'grant_type': 'fb_exchange_token',
        'client_id': app_id,
        'client_secret': app_secret,
        'fb_exchange_token': fb_access_token,
    }

    # Wywołanie żądania
    response = requests.get(
        'https://graph.facebook.com/oauth/access_token', params=params)

    print(response.text)


def fb_get_page_access_token():
    ''' Get page access token.'''
    pageAccessToken = None
    pageId = None

    # Parametry żądania
    params = {
        'fields': 'access_token',
        'access_token': fb_access_token,
    }

    # Wywołanie żądania
    response = requests.get(
        f'https://graph.facebook.com/{fb_page_id}', params=params)

    # If access_token in response and response is not None
    if ('access_token' in response.json()) and (response.json()['access_token'] is not None):
        pageAccessToken = response.json()['access_token']
        pageId = response.json()['id']

        print(f'Page {pageId} received access token {pageAccessToken}.')

    return pageAccessToken


def fb_page_add_post(text: str,
                     image_url: str = None,
                     pageAccessToken: str = None):
    ''' Post text to facebook page. '''
    # Parametry żądania
    params = {
        'message': text,
        'access_token': pageAccessToken,
    }

    # Post message and image
    attachment = {'message': text}
    if (image_url is not None):
        attachment['link'] = image_url

    # Wywołanie żądania
    response = requests.post(
        f'https://graph.facebook.com/{fb_page_id}/feed', params=params)

    return response.text


def main():
    ''' Test facebook post. '''
    # If only FB_ACCESS_TOKEN_SHORTLIVE is set, get new long live access token
    #
    # fb_get_longlive_access_token()

    # Get page access token from facebook access token
    pageAccessToken = fb_get_page_access_token()
    if (pageAccessToken is None):
        raise ValueError('Cannot get page access token.')

    # Post message to facebook page
    response = fb_page_add_post('Test post from python script.',
                                image_url=None,
                                pageAccessToken=pageAccessToken)
    print(response)


if __name__ == '__main__':
    main()
