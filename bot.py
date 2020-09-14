import tweepy

auth = tweepy.OAuthHandler('DkgxPUQEcWAm7MDIbrq5DUsBR', 'WbvGUxnGDr0jFZCgESYQ6kQEEZI8OD5p2BdH0vxVwdmCqiT2x2')
auth.set_access_token('1271397641457332224-HRE3X0K0V3UGpdATxvSy9PtNp5KK9K', 'axdU0Xx14m79orXJi4rBQNS2LsbNhtPCN4sSERsbGMcgC')

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)