from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import Sentiment_module as s

tweet_output = "/home/subhakr/PycharmProjects/Learning NLTK/twitter_output/"

# consumer key, consumer secret, access token, access secret.
ckey = "LFoc70qPtRAjbx0NGDBE3b35W"
csecret = "NXbxiEhZWyMaoAHCLAcSfIRyRtyaetZQyhMWcBYDfRvqF3l8pd"
atoken = "388155336-qI6FsvJnLls5RGKe3GPYStAk3FCiXQ1c4Sh9NJ8j"
asecret = "RS5842o04z1l1B4EvBbPXsGd34ytFeZzvS4OIUqTE5XqD"


class listener(StreamListener):
    def on_data(self, data):
        all_data = json.loads(data)

        tweet = all_data["text"]
        sentiment_value, confidence = s.calculate_sentiment(tweet)
        print(tweet, sentiment_value, confidence)

        if confidence * 100 >= 70:
            output = open(tweet_output + "twitter-out.txt", "a")
            output.write(str(tweet))
            output.write('\n')
            output.write(str(sentiment_value))
            output.write('\n')
            output.write(str(confidence))
            output.write('\n\n\n')
            output.close()
        return True

    def on_error(self, status):
        print(status)


auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

search_key = str(input("Enter a name to be searched in twitter: "))

twitterStream = Stream(auth, listener())
twitterStream.filter(track=[search_key])
