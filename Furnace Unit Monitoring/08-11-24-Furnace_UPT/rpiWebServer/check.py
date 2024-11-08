import time
from datetime import datetime


while True:
	now = datetime.now()
	current_time=now.strftime("%I:%M:%S:%P")
	print("TIME : " + current_time)
	current_date=now.strftime("%d-%m-%Y")
	print("DATE : " + current_date)

	h=now.strftime("%H")
	hour=str(h)
	print(hour)
	f = open("demofile2.txt", "w")
	f.write(current_time)
	f.close()
	time.sleep(1)
