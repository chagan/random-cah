import twitter, random, key

cah = open('cardlist.csv','rb')
cardlist = []

for row in cah.readlines():
    cardlist.append(row.strip())

api = twitter.Api()

api = twitter.Api(consumer_key=key.consumer_key,consumer_secret=key.consumer_secret,access_token_key=key.access_token,access_token_secret=key.access_token_secret)

length = len(cardlist)

status=api.PostUpdate(cardlist[random.randint(0,length)])