#!/usr/bin/env python3

# ask for folder dir
# scan files in folder
# not recursively
#	put files in dictionary
#		what do i use as key?
#		anime name
#			horriblesubs, format is known: "[HorribleSubs] Anime Name - EpNo [quality].mkv"
#			JYFanSubs and LKSub, format is known: "[SubGroup][Anime Name][EpiNo][quality][file type].filetype"
#		what the value?
#			all files that contains that anime name
#				Q: what if you contain different sub groups or quality of the same anime
#				A: TBA
#	ask for dir to save folder
# 	create a folder for each key in dictionary
#		if folder exists
#			skip
#		move all array/list items into folder
#			if file exists and size is same
#				over ride
#			else
#				skip

import os, re, shutil

def cleanPrint():
	for key, value in anime_dict.items():
		print(key+"\n#####")
		value = value.split("#")
		print("\n".join(value))

#from tkinter import filedialog

#might use filedialog for selection
#directory = filedialog.askdirectory(initialdir=os.getcwd(),title="Select folder to sort")

input_dir = "F:\\热播"
sorted_dir = "F:\\热播\\Organized"
anime_dict = {}

while not os.path.isabs(input_dir):
	input_dir = input("Enter folder location to be sort: C:/Users/JohnnyKaime/ \n")

while not os.path.isabs(sorted_dir):
	sorted_dir = input("Enter folder location for files and folders to be moved: C:/Users/JohnnyKaime/Sorted \n")

for root, dirs, files in os.walk(os.path.abspath(input_dir)):

	for file in files:
		if file.endswith(('.mkv','.mp4')):
			#Conditions
			anime_name = file
			clean_anime_name = ""
			if "HorribleSubs" in file:
				clean_anime_name = re.sub("[\(\[].*?[\)\]]", "", anime_name)
				clean_anime_name = clean_anime_name.split("-")[0].strip()
			elif "JYFanSub" in file or "LKSUB" in file or "KTXP" in file:
				clean_anime_name = re.findall('\[(.*?)\]',anime_name)[1]

			if clean_anime_name not in anime_dict:
				anime_dict[clean_anime_name] = os.path.join(root, file)
			else:
				anime_dict[clean_anime_name] = anime_dict[clean_anime_name]+"#"+os.path.join(root, file)
	#Dont want to go into sub folders
	break
#print(list_directories)

for key, value in anime_dict.items():
	if not os.path.exists(os.path.join(sorted_dir,key)):
		os.makedirs(os.path.join(sorted_dir,key))

	anime_list = value.split("#")
	for episode in anime_list:
		shutil.move(episode,os.path.join(sorted_dir,key))
