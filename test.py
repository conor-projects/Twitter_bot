import random


sentence = ["hello {name}" , "{name} hello"]

def hello():
    sentence = ["hello {name}" , "{name} hello"]
    for words in sentence:
        text_file = open("reply_tweet_ids.txt", "a")
        text_file.write(words+ "\n")
        text_file.close()


hello()