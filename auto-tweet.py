# coding=utf-8
import twitter
import time
import random

# IN ORDER TO MAKE THIS SCRIPT WORK, YOU HAVE TO COMPLETE THE FOLLOWING FOUR VALUES
# You can get your consumer and token keys here : https://apps.twitter.com/app/

api = twitter.Api(consumer_key='consumer_key',
                  consumer_secret='consumer_secret',
                  access_token_key='access_token_key',
                  access_token_secret='access_token_secret')

# You can edit the messages sent to women and men here :

message_homme = "Pourquoi n'étiez-vous pas présent lundi à l'Assemblée pour le vote concernant l’état d’urgence ?"
message_femme = "Pourquoi n'étiez-vous pas présente lundi à l'Assemblée pour le vote concernant l’état d’urgence ?"


# #
# The following is the actual code. Do not edit it, unless you know what you're doing of course :)
# #

def send_tweet(deputy_name, message):
    status = api.PostUpdate(".@" + deputy_name + " " + message)
    print("Tweet envoyé à @" + deputy)
    # This next line gives a random number between 25 and 40
    # I decided to use this waiting interval because Twitter does not document their rate limiting for status update
    # in detail. The only information we have is 2400 tweets/day maximum, which is approximately one tweet every 36s.
    wait_time = random.randrange(25 * 10, 40 * 10) / float(10)
    time.sleep(wait_time)


if __name__ == '__main__':
    if api:
        f = open('twitter-accounts-deputes-hommes.txt', 'r')
        deputies = [line.strip() for line in f]
        for deputy in deputies:
            send_tweet(deputy, message_homme)
        f = open('twitter-accounts-deputes-femmes.txt', 'r')
        deputies = [line.strip() for line in f]
        for deputy in deputies:
            send_tweet(deputy, message_femme)
