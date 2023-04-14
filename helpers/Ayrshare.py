from ayrshare import SocialPost
import os

# Get AYRshare API Key
apikey = os.environ.get('AYRSHARE_API_KEY', None)
if (apikey is None):
    raise ValueError('AYRshare API Key not found in env.')


def post_to_social_media(postText: str,
                         platforms: list = None,
                         ):
    ''' Post to social media.'''
    # Default platforms only facebook
    if (platforms is None):
        platforms = ['facebook']

    # Create SocialPost object
    social = SocialPost(apikey)
    # Post to Platforms Twitter, Facebook, and LinkedIn
    postResult = social.post({'post': postText,
                              'platforms': platforms})
    return postResult


if __name__ == '__main__':
    result = post_to_social_media('Test post from AYRshare API.')
    print(result)
