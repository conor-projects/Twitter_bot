import tweepy
import Tkinter
import random
import threading
import time
from tweepy.streaming import StreamListener

consumer_key = 'CONSUMER_KEY'
consumer_secret = 'CONSUMER_SECRET'
access_token = 'ACCESS_TOKEN'
access_token_secret = 'ACCESS_TOKEN_SECRET'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

user = api.me()



def thread_1():
    while True:
        stuff = api.user_timeline(screen_name = 'realDonaldTrump', count = 1, include_rts = True)
        old_tweet_id = open("last_tweet_id.txt", "r")
        for status in stuff:
            with open('last_tweet_id.txt', 'r') as myfile:
                old_tweet_id = myfile.read().replace('\n', '')
                print(old_tweet_id)
                if old_tweet_id == str(status.id):
                    print("no new tweets, taking a 5 minute break")
                    time.sleep(300)
                else:
                    sentence_1 = ["you","you are a","you're a","christ almighty you", "oohhh you", "christ you""mother of god","Jaysus you're a","",]
                    sentence_2 = ["feckin","complete","complete and utter","total","", "absolute", "absolute feckin", "feckin absolute", "feckin complete"]
                    sentence_3 = ["gobshite","numpty","moron","gowal","tik","thick","twat", "dope", "amadan", "simpleton", "feck arse", "silly billy", "dzope", "twonk", "weak man"]
                    print("Found new tweet:'" + status.text + "' with status id: " + str(status.id))
                    print("sending a reply...")
                    tweet = random.choice(sentence_1) + " " + random.choice(sentence_2) + " " + random.choice(sentence_3)
                    print("sending tweet: " + tweet)
                    new_tweet_id = str(status.id)
                    text_file = open("last_tweet_id.txt", "w")
                    text_file.write(new_tweet_id)
                    text_file.close()
                #send tweet
                    api.update_status("@realdonaldtrump " + tweet, in_reply_to_status_id = status.id)

def thread_2():
    while True:
        for mentions in tweepy.Cursor(api.mentions_timeline).items():
            if "#tellhim" in mentions.text.lower():
                if str(mentions.id) not in open('reply_tweet_ids.txt').read():
                    text_file = open("reply_tweet_ids.txt", "a")
                    mention_tweet = str(mentions.id) + "\n"
                    text_file.write(mention_tweet)
                    text_file.close()
                    # read_reply_id = myfile.read().replace('\n', '')
                    reply = ["{handle} oh I'll feckin tell him", "{handle} I'll let him know", "{handle} oh i'll tell him", "don't worry {handle}, he'll hear the words of the irish people"]
                    print("new tweet request")
                    handle = "@" + mentions.user.screen_name
                    response = " " + random.choice(reply).format(handle=handle)
                    print("responding to tweet: " + response)
                    api.update_status(response, in_reply_to_status_id = mentions.id)
                    print("sending trump a tweet...")
                    reply = "@realDonaldTrump" + mentions.text.replace("#tellhim", "").replace("#TellHim", "").replace("@Big_Sean_Murph", "")
                    api.update_status(reply)
                    print(reply)
                else:
                    print("skipping old tweet")
            else:
                print("not a tell him tweet")
        time.sleep(120)




t1 = threading.Thread(target = thread_1)
t2 = threading.Thread(target = thread_2)

t1.start()
t2.start()
