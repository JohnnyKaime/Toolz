# Tools
A collection of small tools that I coded
inspired by automate the boring stuff

# AnimeFileOrganiser
for the love of anime and waifu's &lt;3

Takes in folder directories then loops through sub folders to organise them
Uses the following fan sub groups:
  KTXP
  JYFanSub
  HorribleSubs
  
 More to be added
 
 
 Scans each file, extracts the anime name, uses the anime name as a key in the dictionary
 The value of the dictionary is the full absolute path to the anime episode
 Creates a folder in target with name of the anime
 Moves all files in value of the dictionary into folder

1.  Other file format can be added under #conditions
2.  Make use of regux to extract names from file format
    (might have to manually adjust that)
3.  Will add other useful functions and generic sort functions
3.1 Video type files move to Video
3.2 music type files move to Music 
etc
