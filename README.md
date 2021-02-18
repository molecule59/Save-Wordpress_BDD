# Save-Wordpress_BDD

Condition d'utilasation de ces scripts:
-Debian10
-Python3
-Appache2 & MySql 8.0




Script python automatique à lancer tous les x temps pour sauvegarder un Wordpress dans un bucket AWS, Et un script semi-automatique pour lancer une sauvegarde manuelle ou lancer un restore d'une ancienne sauvegarde.

Dans les 2 scripts (save.py & restore.py) vous aller retrouver tout en haut les informations sur le projet, puis les imports utilisées suivi de la récupération de la date et de l'heure.


save.py: Vous allez retouver toutes les variables utilisé dance ce script

#Wordpress HTML
wp_html = '/var/www/html/wordpress'

#Wordpress BDD
wp_bdd = '/var/lib/mysql/WP'

racine = "/ScriptPython/"
file_name = "Site-BDD_" + date_Y + "-" + date_m + "-" + date_d + "_" + date_H + "h" + date_M + "m" + date_S + "s"
extension_zip = ".zip"
file_name_zip = racine + file_name + extension_zip

#One space before s3 bucket
BucketAWS = " s3://aic-projet6/"
SendAWS = "aws s3 cp " + file_name_zip + BucketAWS


