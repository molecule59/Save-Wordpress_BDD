# Save-Wordpress_BDD

Condition d'utilasation de ces scripts:
-Debian10
-Python3
-Appache2 & MySql 8.0


Script python automatique à lancer tous les x temps pour sauvegarder un Wordpress dans un bucket AWS, Et un script semi-automatique pour lancer une sauvegarde manuelle ou lancer un restore d'une ancienne sauvegarde.

Dans log.txt vous allez retrouver l'historique des sauvegardes et des backup rélaiser par les 2 scripts avec la date et l'heure.
Dans savelist.txt on retouvre la liste de tout les sauvegardes efffecuer, cette liste sert pour afficher les choix pour resore un wordpress dans restore.py

Dans les 2 scripts (save.py & restore.py) vous aller retrouver tout en haut les informations sur le projet, puis les imports utilisées suivi de la récupération de la date et de l'heure et les variables utilisées et à modfier celon votre configuration.


save.py:




