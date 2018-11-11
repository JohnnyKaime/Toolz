import glob
import os

def readSubGroups():
	with open("SubGroup") as file:
		for line in file:
			(key, val) = line.split()
			SubDict[key] = val
	for group in SubDict:
		print(group)

def findFileSaveToList():
	#currentPath = os.path.dirname(__file__)
    my_path = r"" + input("Which folder? \nIf it's in the current folder enter '.' ")
    files = glob.glob(my_path + '/**/*', recursive=True)
    #print(files[1][2:])
    

SubDict = {}

readSubGroups()
findFileSaveToList()
