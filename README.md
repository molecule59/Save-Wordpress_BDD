# Save-Wordpress_BDD

Condition d'utilasation de ces scripts:
-Debian10
-Python3
-Appache2 & MySql 8.0
-Installer AWScli et configurer un compte qui acces au bucket
https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2-linux.html




Script python automatique à lancer tous les x temps pour sauvegarder un Wordpress dans un bucket AWS. Et un script semi-automatique pour lancer une sauvegarde manuelle ou lancer un restore d'une ancienne sauvegarde.

Dans log.txt vous allez retrouver l'historique des sauvegardes et des backups réaliser par les 2 scripts avec la date et l'heure.
Dans savelist.txt on retrouve la liste de toutes les sauvegardes efffecuer, cette liste sert pour afficher les choix pour resore un wordpress dans restore.py

Dans les 2 scripts (save.py & restore.py) vous allez retrouver tout en haut les informations sur le projet, puis les imports utilisés suivis de la récupération de la date et de l'heure et les variables utilisées et à modifier selon votre configuration.


save.py: Ce script créer un fichier zip nomée "Site-BDD_Date_Heure.zip" avec la variable wp_htm et wp_bdd qui sont les racines du wordpress, puis envoie le fichier zip dans le bucket AWS qui ensuite supprime le fichier zip créer précedament 




