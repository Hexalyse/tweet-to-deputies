# coding=utf-8
import twitter
import time
import random

api = twitter.Api(consumer_key='consumer_key',
                  consumer_secret='consumer_secret',
                  access_token_key='access_token_key',
                  access_token_secret='access_token_secret')

message_homme = "Pourquoi n'étiez-vous pas présent lundi à l'Assemblée pour le vote concernant l’état d’urgence ?"
message_femme = "Pourquoi n'étiez-vous pas présente lundi à l'Assemblée pour le vote concernant l’état d’urgence ?"


def sendTweet(deputy_name, message):
    status = api.PostUpdate(".@" + deputy + " " + message)
    # This next line gives a random number between 25 and 40
    # I decided to use this waiting interval because Twitter does not document their rate limiting for status update
    # in detail. The only information we have is 2400 tweets/day maximum, which is approximately one tweet every 36s.
    wait_time = random.randrange(25 * 10, 40 * 10) / float(10)
    print("Tweet envoyé à @" + deputy)
    time.sleep(wait_time)


if __name__ == '__main__':
    if api:
        f = open('twitter-accounts-deputes-hommes.txt', 'r')
        deputies = [line.strip() for line in f]
        for deputy in deputies:
            sendTweet(deputy, message_homme)
        f = open('twitter-accounts-deputes-femmes.txt', 'r')
        deputies = [line.strip() for line in f]
        for deputy in deputies:
            sendTweet(deputy, message_femme)
