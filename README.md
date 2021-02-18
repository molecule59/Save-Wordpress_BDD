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


save.py: Ce script crée un fichier zip nommé "Site-BDD_Date_Heure.zip" avec la variable wp_html et wp_bdd qui sont les racines du wordpress, puis envoie le fichier zip dans le bucket AWS qui ensuite supprime le fichier zip créer précédemment. Créer le fichier dans les logs.

restore.py: Il y a 3 fonction dans le script un est le main avec le menu princial, la fonction save lance le script save.py et la fonction backup vas afficher les 5 derniers save réaliser avec le script save.py pour pouvoir choisir lequel restorer. Si entre 1 à 5 il va resorer le nom du fichier choisit puis va le télécharger dans le bucket AWS et va l'extraire. Supprime le wordpress (bdd et html) .Puis copier coller les 2 dossiers dans les bons endroits choisir par les variables wp_html et wp_bdd, une fois celà fait on donne les droits classic sur les dossieer et on restart mysql et appache2. Puis enfin on supprime le zip et l'extract du zip et on ajoute au fichier log. Si différent de 1 à 5 retour au main.




