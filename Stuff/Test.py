month_dict = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]

raw_date = input("Enter date: ")
raw_date_format = raw_date.split("-")
new_month = ""
if(len(str(month_dict.index(raw_date_format[1])+1)) == 1):
	new_month = "0"+str(month_dict.index(raw_date_format[1])+1)
else:
	new_month = str(month_dict.index(raw_date_format[1])+1)

new_day = ""
if(len(str(raw_date_format[0])) == 1):
	new_day = "0"+str(raw_date_format[0])
else:
	new_day = str(raw_date_format[0])

raw_counter=0
with open("counter.txt","r") as file:
	raw_counter = int(file.read())

raw_counter+=1
counter = 0
if(len(str(raw_counter)) == 1):
	counter = "00"+str(raw_counter)
elif(len(str(raw_counter)) == 2):
	counter = "0"+str(raw_counter)
else:
	counter = str(raw_counter)

print("E{}{}-{}".format(new_month,"21",counter))

with open("counter.txt","w") as file:
	file.write(str(raw_counter))