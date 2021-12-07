import datetime

londondiff = 8
newyorkdiff = 3

today = datetime.datetime.now()
portlandtime = today.strftime("%H:%M:%S")
newyorktime = int(portlandtime[0:2]) + newyorkdiff
londontime = int(portlandtime[0:2]) + londondiff

print("Portland Time:", portlandtime)

if int(portlandtime[0:2]) <= 9 or int(portlandtime[0:2]) > 18:
	print("Portland Office Closed")
else:
	print("Portland Office Open")
	
	
if londontime <= 9 or londontime > 18:
	print("London Office Closed")
else:
	print("London Office Open")
	
		
if newyorktime <= 9 or newyorktime > 18:
	print("New York Office Closed")
else:
	print("New York Office Open")

#londontime and newyorktime % hoursinday