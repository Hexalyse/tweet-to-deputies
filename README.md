## Script de tweet automatique aux députés absents lors de votes importants

*Attention, ce script est une ébauche créée en 30 minutes, il est loin d'être complet et ne contient aucune gestion d'erreur.*

Suite à la lecture de [cet article](http://www.liberation.fr/france/2016/02/09/etat-d-urgence-demandez-a-votre-depute-pourquoi-il-n-a-pas-vote-lundi_1432146), et vu la quantité considérable de députés absents, je me suis dit "et pourquoi ne pas automatiser l'envoi des tweets ?".

C'est le but de ce script : tweeter un message à l'ensemble des députés absents lors du vote.

**NB: La liste de députés fournie ainsi que le message prédéfini correspond à la liste fournie dans l'article de Libération visible ci-dessus.** Vous pouvez bien évidemment modifier les fichiers `twitter-accounts-deputes-femmes.txt` et `twitter-accounts-deputes-hommes.txt` ainsi que les messages envoyés, selon vos besoin.

Un compte de test a été créé pour l'occasion. Vous pouvez voir le script en action ici (il devrait prendre à peu près 3 heures pour finir sa tâche): https://twitter.com/AlexLeRelou

### Prérequis techniques

Il vous faudra une installation fonctionnelle de Python, ainsi que les librairies suivantes :
* python-twitter
* requests_oauthlib (si vous utilisez le script pour obtenir automatiquement votre Token d'accès, ce qui est optionnel)

Vous pouvez installer ces script avec les commandes suivantes :

    pip install python-twitter
    pip install requests_oauthlib

### Installation

Pour obtenir le script, rien de plus simple :
    
    git clone https://github.com/Hexalyse/tweet-to-deputies.git
    
Et vous n'avez plus qu'à éditer le fichier `auto-tweet.py` comme décrit ci-dessous avant de l'exécuter.

### Ce dont vous aurez besoin avant de lancer le script

Pour faire fonctionner ce script, il vous faudra mettre à jour 4 lignes dans le fichier `auto-tweet.py`:

    api = twitter.Api(consumer_key='twitterConsumerKey',
                      consumer_secret='twitterConsumerSecret',
                      access_token_key='twitterToken',
                      access_token_secret='twitterTokenSecret')
                      
Pour obtenir ces 4 "clés", il vous faudra procéder comme suit :
* Allez sur la page https://apps.twitter.com/app/ pour créer une nouvelle application développeur. Cela vous permettra d'obtenir votre "Consumer Key" et votre "Consumer Secret"
* Une fois l'application créée,vous pouvez générer un token d'accès dans l'onglet "Keys and Access Tokens" de la gestion de votre application. Alternativement, vous pouvez aussi lancer le script `get_access_token.py` qui vous permettra d'obtenir le "Token" et le "Token Secret".

*Pour ceux qui préfèrent un tutoriel en image, en voici un en anglais : http://www.slickremix.com/docs/how-to-get-api-keys-and-tokens-for-twitter/ *

**Vous n'avez plus qu'à renseigner ces 4 valeurs dans le fichier, et à lancer le script ! Enjoy :)**

### Délai d'envoi des tweets

Il semblerait que même en respectant les limites d'envoi de tweet de Twitter, Twitter réussisse à détecter qu'il s'agit d'un envoi automatisé.

Je suis donc passé d'environ 30-40 secondes entre chaque tweet à un temps d'attente de 2 à 4 minutes entre chaque tweet, et cela semble fonctionner.

### Contribution
Ce script a été créé par [@Hexalyse](https://github.com/Hexalyse/).