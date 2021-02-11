import sys, tweepy

def twitter_auth():
    try:
        consumer_key = 'gJGAh2Kja0V1gCOp4OoBuFe4i'
        consumer_secret = 'aqGv25ZrGxYyMfLbdrShdLL3aiGl90af0cc1xo86sJKDPKtwXf'
        access_token = 'AAAAAAAAAAAAAAAAAAAAAFtqHAEAAAAAuo8A8kKea67cj%2FNU57hqSD31dyg%3DevsEy0FYjsVm2AaysJfStyeu081ZdA2uXDG09NZEKfNVQ3Y1hY'
        access_secret = 'xxxxxxxxxxxxxxxxxx'
    except KeyError:
        sys.stderr.write("TWITTER_* environment variable not set \n")
        sys.exit(1)
    auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token,access_secret)
    return auth

def get_twitter_client():
    auth = twitter_auth()
    client = tweepy.API(auth, wait_on_rate_limit=True)
    return client

if __name__ == "__main__":
    user = input("Enter name : ")
    client = get_twitter_client()
    for status in tweepy.Cursor(client.home_timeline, screen_name = user).items(1):
        print(status.text)







