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
import tkinter
from tkinter import filedialog
from tkinter import messagebox

input_dir = ""
sorted_dir = ""
anime_dict = {}

def cleanPrint():
	for key, value in anime_dict.items():
		print(key+"\n#####")
		value = value.split("#")
		print("\n".join(value))

def askForDir():
	#might use filedialog for selection
	temp_dir = ""
	while not os.path.isabs(temp_dir):
		temp_dir = filedialog.askdirectory(initialdir=os.getcwd(),title="Select folder to sort")
	global input_dir
	input_dir = temp_dir.replace("/","\\\\")
	temp_dir = ""
	while not os.path.isabs(temp_dir):
		temp_dir = filedialog.askdirectory(initialdir=os.getcwd(),title="Select folder to be sorted")
		global sorted_dir
	sorted_dir = temp_dir.replace("/","\\\\")

def scan():
	for root, dirs, files in os.walk(os.path.abspath(input_dir)):

		for file in files:
			if file.endswith(('.mkv','.mp4')):
				#Conditions
				anime_name = file
				clean_anime_name = ""
				if "horriblesubs" in file.lower():
					clean_anime_name = re.sub("[\(\[].*?[\)\]]", "", anime_name)
					clean_anime_name = clean_anime_name.split("-")[0].strip()
				elif "jyfansub" in file.lower() or "lksub" in file.lower() or "ktxp" in file.lower():
					clean_anime_name = re.findall("\[(.*?)\]",anime_name)[1]
				elif "erai-raws" in file.lower():
					clean_anime_name = re.findall('\](.*?)\[',anime_name);
					lastOccurOfHyphen = clean_anime_name[0].rindex("-");
					clean_anime_name = clean_anime_name[0][:lastOccurOfHyphen].strip()

				if clean_anime_name not in anime_dict:
					anime_dict[clean_anime_name] = os.path.join(root, file)
				else:
					anime_dict[clean_anime_name] = anime_dict[clean_anime_name]+"#"+os.path.join(root, file)
		#Dont want to go into sub folders
		#Uncomment if you want
		break
	#print(list_directories)

def move():
	for key, value in anime_dict.items():
		if not os.path.exists(os.path.join(sorted_dir,key)):
			os.makedirs(os.path.join(sorted_dir,key))

		anime_list = value.split("#")
		for episode in anime_list:
			shutil.move(episode,os.path.join(sorted_dir,key))

askForDir()
scan()
move()
messagebox.showinfo("Completed", "All files are sorted from dir: {}\nto\ndir: {}".format(input_dir,sorted_dir))
