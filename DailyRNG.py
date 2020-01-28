import datetime
import random

listOfPlaces = ["Hot Chips","Life Science Daily Meals","Sushi","Chinese","Crossant","A Block Burger and Chips","Pie","Panini","LS Burger and Chips","LS Chichenpops","McD","MrD"]

RNG = random.randint(0, len(listOfPlaces)-1)
print(listOfPlaces[RNG])

f = open("RNG.txt","a+")
f.write(str(datetime.datetime.now())+"\n")
f.write(listOfPlaces[RNG]+"\n\n")
f.close()