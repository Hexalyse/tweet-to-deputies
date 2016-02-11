# Auto tweet absent French deputies

*Attention, ce script est une ébauche créée en 30 minutes, il est loin d'être complet et ne contient aucune gestion d'erreur.*

Suite à la lecture de [cet article](http://www.liberation.fr/france/2016/02/09/etat-d-urgence-demandez-a-votre-depute-pourquoi-il-n-a-pas-vote-lundi_1432146), et vu la quantité considérable de députés absents, je me suis dit "et pourquoi ne pas automatiser l'envoi des tweets ?".

C'est le but de ce script : tweeter un message à l'ensemble des députés absents lors du vote qui possèdent un compte Twitter.

## Prérequis techniques
Il vous faudra une installation fonctionnelle de Python, ainsi que les librairies suivantes :
* python-twitter
* requests_oauthlib (si vous utilisez le script pour obtenir automatiquement votre Token d'accès, ce qui est optionnel)

## Ce dont vous aurez besoin

Pour faire fonctionner ce script, il vous faudra mettre à jour 4 lignes dans le fichier `auto-tweet.py`:

    api = twitter.Api(consumer_key='twitterConsumerKey',
                      consumer_secret='twitterConsumerSecret',
                      access_token_key='twitterToken',
                      access_token_secret='twitterTokenSecret')
                      
Pour obtenir ces 4 "clés", il vous faudra procéder comme suit :
* Allez sur https://apps.twitter.com/app/ pour créer une nouvelle application développeur. Cela vous permettra d'obtenir votre "Consumer Key" et votre "Consumer Secret"
* Une fois ces 2 clés obtenues, lancez le script `get_access_token.py` qui vous permettra d'obtenir le "Token" et le "Token Secret". Vous pouvez également faire ça à la main sur la page de gestion de vos Consumer keys.


Vous n'avez plus qu'à renseigner ces 4 valeurs dans le fichier, et à lancer le script ! Enjoy :)
