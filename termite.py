# Python3 version of Termite Credential Hunter
import argparse
import os

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

matchValues = ["creds", "credentials", "password","passwd", "logon"]

def draw_logo():
	print(bcolors.OKGREEN+"""
░▒▓████████▓▒░▒▓████████▓▒░▒▓███████▓▒░░▒▓██████████████▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓████████▓▒░ 
   ░▒▓█▓▒░   ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░  ░▒▓█▓▒░   ░▒▓█▓▒░        
   ░▒▓█▓▒░   ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░  ░▒▓█▓▒░   ░▒▓█▓▒░        
   ░▒▓█▓▒░   ░▒▓██████▓▒░ ░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░  ░▒▓█▓▒░   ░▒▓██████▓▒░   
   ░▒▓█▓▒░   ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░  ░▒▓█▓▒░   ░▒▓█▓▒░        
   ░▒▓█▓▒░   ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░  ░▒▓█▓▒░   ░▒▓█▓▒░        
   ░▒▓█▓▒░   ░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░  ░▒▓█▓▒░   ░▒▓████████▓▒░ 
                                                                                             
                                                                                             
"""+bcolors.ENDC)


def get_folders(rootFolder):
	folders = []
	try:
		for (root, dirs, file) in os.walk(rootFolder):
			folders.append(root)
	except Exception as e:
		print(bcolors.FAIL+"FAILED TO WALK PATH:  "+rootFolder)
		print(bcolors.WARNING,e,bcolors.ENDC)
	return folders


def get_files(folders):
	global matchValues

	for folder in folders:
		interestingFiles = []
		for file in  os.listdir(folder):
			search_file(file, folder)
			if(file in matchValues):
				interestingFiles.append(file)
		if(interestingFiles):
			print(bcolors.OKGREEN+"INTERSTING FILES IN:  "+bcolors.OKCYAN+folder)
			for interest in interestingFiles:
				print(bcolors.WARNING+file+bcolors.ENDC+"\n")

def search_file(fileName, path):
	global matchValues
	realPath = path+"/"+fileName

	try:
		with open(realPath, 'r') as file:
			lineNumber = 1
			for line in file:
				for item in matchValues:
					if( item.lower() in line.lower() ):
						print(bcolors.OKBLUE+"MATCH FOUND!\n"+bcolors.OKCYAN+"FILE:  "+bcolors.ENDC+realPath+bcolors.OKCYAN+"\nLine Number:  "+bcolors.ENDC,lineNumber)
						if(len(line) > 200):
							print(bcolors.WARNING+"LINE TOO LONG TO PRINT\n"+bcolors.ENDC)
						else:
							print(bcolors.WARNING+line+bcolors.ENDC)
						break
				lineNumber += 1
		file.close()
	except Exception as e:
		if("Is a directory" not in str(e) and "decode byte" not in str(e)):
			print(bcolors.FAIL+"Failed To Open File:  "+realPath)
			print(bcolors.WARNING,e,bcolors.ENDC+"\n")


def main():
	global matchValues

	path = "./"
	ctf = False
	hash = None
	username = None
	usernameList = None
	password = None
	passwordList = None
	hashFile = None
	folders = []

	msg = "python3 version of Termite Credential Hunter"

	parser = argparse.ArgumentParser(description = msg)
	parser.add_argument("-f","--path", help = "Set Search Path")
	parser.add_argument("-c","--ctf", help = "Turn On CTF Mode")
	parser.add_argument("-s","--hash", help = "When CTF Mode Is On, Limit Search Based On Flag Hash Type")
	parser.add_argument("-u","--username", help = "Include A Know Username To Help Target Search")
	parser.add_argument("-U","--usernameList", help = "Set A File Path Containing Usernames")
	parser.add_argument("-p","--password", help = "Include A Know Password To Help Target Search")
	parser.add_argument("-P","--passwordList", help = "Set A File Path Containing Passwords")
	parser.add_argument("-o","--output", help = "Set An Output File")
	parser.add_argument("--hashFile", help = "Set A Comparative List Of Hash Files To Ignore Common Files")

	args = parser.parse_args()

	if(args.path != None):
		path = args.path

	if(args.username != None):
		matchValues.append(args.username)

	if(args.password != None):
		matchValues.append(args.password)

	draw_logo()
	folders = get_folders(path)
	get_files(folders)

main()
