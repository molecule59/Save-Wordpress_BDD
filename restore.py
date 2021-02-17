import os
import shutil
from zipfile import ZipFile
import datetime
import time
import linecache

#Recup Date & Hour ----------------------------------------------------------------------------------------------------
date = datetime.datetime.now()

date_Y = str(date.year)
date_m = str(date.month)
date_d = str(date.day)
date_H = str(date.hour)
date_M = str(date.minute)
date_S = str(date.second)

date_hours = date_Y + "-" + date_m + "-" + date_d + "_" + date_H + "h" + date_M + "m" + date_S + "s"

#Variable -----------------------------------------------------------------
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
#Source apache2
dst_html = "/var/www/html/"
#Source MySQL
dst_bdd = "/var/lib/mysql/"
#Bucket AWS
bucket = "s3://aic-projet6/"
extension_zip = ".zip"



print("I will backup your site before you use this script")


def main():
	#---------- MAINE - MENU ----------
	print (30 * '\033[31m-\033[0m')
	print ("\033[31m             MENU\033[0m")
	print (30 * '\033[31m-\033[0m')
	print("1. Save manually\n")
	print("2. Backup\n")
	print(". Press any touch for Exit")
	print (30 * '\033[31m-\033[0m')

	choice = input("Enter your choice: ")
	#choice = int(choice)
	if (choice == "1"):
		save()
		main()

	elif(choice == "2"):
		print("I will save your site before you backup your site")
		save()
		backup()
		main()
	else:
		exit()


def save():
	#Backup
	os.system("python3 " + racine + "save.py")



def backup():
	#Menu
	print (30 * '\033[31m-\033[0m')
	print ("\033[31m            BACKUP\033[0m")
	print (30 * '\033[31m-\033[0m')
	print ("1. " + linecache.getline(racine + "savelist.txt",1))
	print ("2. " + linecache.getline(racine + "savelist.txt",2))
	print ("3. " + linecache.getline(racine + "savelist.txt",3))
	print ("4. " + linecache.getline(racine + "savelist.txt",4))
	print ("5. " + linecache.getline(racine + "savelist.txt",5))
	print ("9. For Exit")
	print (30 * '\033[31m-\033[0m')
	 
	#Choice Menu
	choice2 = int(input("Enter your choice: "))



	if (choice2 == 1 or choice2 ==2 or choice2 ==3 or choice2 ==4 or choice2 ==5):
		#Define the File Name with the savelist.txt and number of the line choose
		file_nameN = linecache.getline(racine + "savelist.txt",choice2)
		#File Name string
		file_nameN = str(file_nameN)
		#Remove back to line after the name of the file name
		file_name = file_nameN.rstrip('\n')


		#dowload file from AWS
		os.system("aws s3 cp " + bucket + file_name + extension_zip + " " + racine)

		#Extract zip file in folder with the same name
		with ZipFile(racine + file_name + extension_zip, 'r') as zip: 
			zip.extractall(racine + file_name)

		#src_html = racine + file_name + name_html
		#src_bdd = racine + file_name + name_bdd

		#Delete folder Wordpress html & BDD
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
		logW.write("BACKUP	" + file_name + ".zip" + "		THE: " + date_hours + "\n" + text)
		logW.close()

	else:
		main()

#Scénario ------------------------------------------------------------------------------------------
main()


