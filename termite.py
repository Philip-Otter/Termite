# Python3 version of Termite Credential Hunter
# Made with love 
# 2xdropout 2024
import argparse
import os
import re

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
ctfIndicatorValues = ["ctf","flag","picoctf","htb"]
ignoredHashes = []
ctf = False
hashFile = None

def draw_logo():
	print(bcolors.OKGREEN+"""
--------------------------------------------------------------
|							     |
|  ████████╗███████╗██████╗ ███╗   ███╗██╗████████╗███████╗  |
|  ╚══██╔══╝██╔════╝██╔══██╗████╗ ████║██║╚══██╔══╝██╔════╝  |
|     ██║   █████╗  ██████╔╝██╔████╔██║██║   ██║   █████╗    |
|     ██║   ██╔══╝  ██╔══██╗██║╚██╔╝██║██║   ██║   ██╔══╝    |
|     ██║   ███████╗██║  ██║██║ ╚═╝ ██║██║   ██║   ███████╗  |
|     ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝   ╚═╝   ╚══════╝  |
--------------------------------------------------------------
"""+bcolors.ENDC)


def ctf_search(fileName, path):
	global ctfIndicatorValues

	realPath = path+"/"+fileName

	try:
		with open(realPath, 'r', errors = "ignore") as file:
			lineNumber = 1
			for line in file:
				for item in ctfIndicatorValues:
					reSearch = item+"\W\w+\W"
					hits = re.findall(str(reSearch), line.lower())
					if(hits):
						print(bcolors.OKBLUE+"MATCH FOUND!\n"+bcolors.OKCYAN+"FILE:  "+bcolors.ENDC+realPath+bcolors.OKCYAN+"\nLine Number:  "+bcolors.ENDC,lineNumber)
						for hit in hits:
							print(bcolors.WARNING+str(hit))
						print("\n"+bcolors.ENDC)
				lineNumber += 1
		file.close()
	except Exception as e:
		print(bcolors.FAIL+"FAILED TO SEARCH FOR CTF FLAG MATCH IN FILE:  "+realPath)
		print(bcolors.WARNING,e,"\n"+bcolors.ENDC)


def import_hashes():  # Need to comeback later to have this accept more than just newline seperated hashes
	global hashFile
	global ignoredHashes

	try:
		with open(hashFile,'r') as file:
			for line in file:
				ignoredHashes.append(line.strip())
		file.close()
	except Exception as e:
		print(bcolors.FAIL+"FAILED TO IMPORT HASH LIST FROM FILE:  "+hashFile)
		print(bcolors.WARNING,e,"\n"+bcolors.ENDC)


def import_matchValues(filePath):
	global matchValues

	try:
		with open(filePath,'r') as file:
			for line in file:
				matchValues.append(line.strip())
		file.close()
	except Exception as e:
		print(bcolors.FAIL+"FAILED TO IMPORT USERNAME OR PASSWORD LIST:  "+filePath)
		print(bcolors.WARNING,e,"\n"+bcolors.ENDC)


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
	global ctf

	for folder in folders:
		interestingFiles = []
		for file in  os.listdir(folder):
			if(ctf):
				ctf_search(file,folder)
			else:
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
	global ctf
	global hash
	global hashFile

	path = "./"
	username = None
	usernameList = None
	password = None
	passwordList = None
	folders = []

	msg = "python3 version of Termite Credential Hunter"

	parser = argparse.ArgumentParser(description = msg)
	parser.add_argument("-f","--path", help = "Set Search Path")
	parser.add_argument("-c","--ctf", action = "store_true", help = "Turn On CTF Mode")
	parser.add_argument("-u","--username", help = "Include A Know Username To Help Target Search")
	parser.add_argument("-U","--usernameList", help = "Set A File Path Containing Usernames")
	parser.add_argument("-p","--password", help = "Include A Know Password To Help Target Search")
	parser.add_argument("-P","--passwordList", help = "Set A File Path Containing Passwords")
	parser.add_argument("-o","--output", help = "Set An Output File")
	parser.add_argument("--hashFile", help = "Set A Comparative List Of Hash Files To Ignore Common Files")

	draw_logo()

	args = parser.parse_args()

	if(args.path != None):
		path = args.path

	if(args.username != None):
		matchValues.append(args.username)

	if(args.password != None):
		matchValues.append(args.password)

	if(args.usernameList != None):
		import_matchValues(args.usernameList)

	if(args.passwordList != None):
		import_matchValues(args.passwordList)

	if(args.usernameList != None):
		import_matchValues(args.usernameList)

	if(args.hashFile != None):
		import_hashes()

	if(args.ctf == True):
		ctf = True

	folders = get_folders(path)
	get_files(folders)

main()
