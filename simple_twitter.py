#Taken from http://stackoverflow.com/questions/6399978/getting-started-with-twitter-oauth2-python

import oauth2 as oauth
import json
import time
import minishift
import time
import keys

def notify(tweet):

    width = 8*3
    vid, pid = 0x04d8, 0xf517

    ms = minishift.Minishift(minishift.MCP2210Interface(vid, pid), width)
    canvas = minishift.Canvas()
    canvas.write_text(0,tweet)
    for i in range(0, 5):
        for slice in canvas.scroll():
            ms.update(slice)
            time.sleep(0.05)

    
    

consumer = oauth.Consumer(key=keys.CONSUMER_KEY, secret=keys.CONSUMER_SECRET)
access_token = oauth.Token(key=keys.ACCESS_KEY, secret=keys.ACCESS_SECRET)
client = oauth.Client(consumer, access_token)

timeline_endpoint = "https://api.twitter.com/1.1/statuses/mentions_timeline.json"


lastMention = str()



while(1):
    response, data = client.request(timeline_endpoint)
    tweets = json.loads(data.decode())




    if tweets[0]['text'] == lastMention:
        time.sleep(10)
        continue
    else:
        lastMention = tweets[0]['text']

        notify(lastMention)



