 #Import --------------------------------------------------------------------------------------------------------------
import shutil 
from zipfile import ZipFile
import zipfile
import os
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

date_time = date_Y + "-" + date_m + "-" + date_d + "_" + date_H + "h" + date_M + "m" + date_S + "s"

#Variable -------------------------------------------------------------------------------------------------------------
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


#Creation du fichier zip ----------------------------------------------------------------------------------------------
def zipdir(path, ziph):
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), os.path.join(path, '..')))
  
if __name__ == '__main__':
    zipf = zipfile.ZipFile(file_name_zip, 'w', zipfile.ZIP_DEFLATED)
    zipdir(wp_html, zipf)
    zipdir(wp_bdd, zipf)
    zipf.close()
print("Zip file is create and name is: " + file_name)

#Send zip file to AWS bucket = aic-projet6 --------------------------------------------------------------------------------------
print("Zip file is Sending")
os.system(SendAWS)
print("Zip file send successfully")

#Delete files create  ---------------------------------------------------------------------------------------------------
os.remove(file_name_zip)
print("Files for create zip are delete")

#Add in log file
logR = open(racine + "log.txt", "r")
text = logR.read()
logR.close()
 
logW = open(racine + "log.txt", "w")
logW.write("SAVE	" + file_name + ".zip" + "\n" + text)
logW.close()


#Add file name save
fileR = open(racine + "savelist.txt", "r")
text = fileR.read()
fileR.close()
 
fileW = open(racine + "savelist.txt", "w")
fileW.write(file_name + "\n" + text)
fileW.close()
