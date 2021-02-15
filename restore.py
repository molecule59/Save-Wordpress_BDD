import os
import shutil
from zipfile import ZipFile
import datetime
import time

#Recup Date & Hour ----------------------------------------------------------------------------------------------------
date = datetime.datetime.now()

date_Y = str(date.year)
date_m = str(date.month)
date_d = str(date.day)
date_H = str(date.hour)
date_M = str(date.minute)
date_S = str(date.second)

date_hours = date_Y + "-" + date_m + "-" + date_d + "_" + date_H + "h" + date_M + "m" + date_S + "s"

#variable -----------------------------------------------------------------
#Source of your script
racine = "/ScriptPython/"
#Source of yout folder apache2
wp_html = "/var/www/html/wordpress/"
#Source of your BDD in mysql
wp_bdd = "/var/lib/mysql/WP/"
#Name of folder html
name_html = "/wordpress"
#Name of folder BDD
name_bdd = "/WP"
dst_html = "/var/www/html/"
dst_bdd = "/var/lib/mysql/"
extension_zip = ".zip"


print("Welcome on the script for restore Site and BDD")
print("I will backup your site before you use this script")
os.system("python3 " + racine + "save.py")


#Input name of save
file_name = input("Entrée le nom du fichier (sans l'extension): ")

#dowload file from AWS
os.system("aws s3 cp s3://aic-projet6/" + file_name + extension_zip + " " + racine)

#Extract zip file in folder with the same name
with ZipFile(racine + file_name + extension_zip, 'r') as zip: 
	zip.extractall(racine + file_name)

src_html = racine + file_name + name_html
src_bdd = racine + file_name + name_bdd

os.system("rm -rf " + wp_html )
os.system("rm -rf " + wp_bdd )



#Copy html & BDD for the unzip folder in apache2 & mysql
os.system("cp -r " + racine + file_name + name_html + " " + dst_html )
os.system("cp -r " + racine + file_name + name_bdd + " " + dst_bdd)

#Give a normally riht for the folder
os.system("chown -R www-data:www-data " + wp_html)
os.system("chmod 755 -R " + wp_html)
os.system("chown -R mysql:mysql " + wp_bdd)

#Restart apache2 & mysql
os.system("systemctl restart apache2")
os.system("systemctl restart mysql")


#Delete folder and zip files create
os.system("rm -r " + racine + file_name )
os.system("rm -r " + racine + file_name + extension_zip)


#Add in log file
logR = open(racine + "log.txt", "r")
text = logR.read()
logR.close()
 
logW = open(racine + "log.txt", "w")
logW.write("BACKUP	" + file_name + ".zip" + "	THE: " + date_hours + "\n" + text)
logW.close()