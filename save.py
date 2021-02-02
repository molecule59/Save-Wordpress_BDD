 #Import --------------------------------------------------------------------------------------------------------------
import shutil 
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


#Variable -------------------------------------------------------------------------------------------------------------
srcSite = '/var/www/html'
dstSite = '/ScriptPython/tmp/Site'
srcBDD = '/var/lib/mysql/wordpress'
dstBDD = '/ScriptPython/tmp/BDD'

lien_date_zip = "/ScriptPython/tmp/"
name_date_zip = "Site-BDD_" + date_Y + "-" + date_m + "-" + date_d + "_" + date_H + "h" + date_M + "m" + date_S + "s"
extension_zip = ".zip"
file_date_zip = lien_date_zip + name_date_zip + extension_zip


#Copy Site & BDD in tree tmp ------------------------------------------------------------------------------------------
shutil.copytree(srcSite, dstSite)
shutil.copytree(srcBDD, dstBDD)


#Creation du fichier zip ----------------------------------------------------------------------------------------------
def zipdir(path, ziph):
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), os.path.join(path, '..')))
  
if __name__ == '__main__':
    zipf = zipfile.ZipFile(file_date_zip, 'w', zipfile.ZIP_DEFLATED)
    zipdir('/ScriptPython/tmp/BDD', zipf)
    zipdir('/ScriptPython/tmp/Site', zipf)
    zipf.close()
print("Zip file is create and name is: " + name_date_zip)

#Send zip file to AWS bucket = aic-projet6 --------------------------------------------------------------------------------------
print("Zip file is Sending")
SendAWS = "aws s3 cp " + file_date_zip + " s3://aic-projet6/"
os.system(SendAWS)
print("Zip file send successfully")

#Delete files in tmp ---------------------------------------------------------------------------------------------------
shutil.rmtree(dstSite)
shutil.rmtree(dstBDD)
os.remove(file_date_zip)
print("Files in tmp are delete")