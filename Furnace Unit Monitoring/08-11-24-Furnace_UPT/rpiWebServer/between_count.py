import time
from datetime import datetime

while True:
    FULL="04:08:30:pm"
    DAY="04:08:40:pm"
    HALF="04:08:55:pm"

    now = datetime.now()
    current_time=now.strftime("%I:%M:%S:%P")
    print("TIME : " + current_time)
    current_date=now.strftime("%d-%m-%Y")
    print("DATE : " + current_date)

    h=now.strftime("%H")
    hour=int(h)
    print(hour)

    a=0
    b=8
    c=16
    r=int(input("enter number:"))




    if a < r:
        print("full")
    if r < b:
        print("DAY")
    if c < r:
        print("half")
    time.sleep(1)
