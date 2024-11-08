import time
from datetime import datetime

while True:          
        FULL= "04:08:30:pm"
        DAY="04:08:40:pm"
        HALF="04:08:55:pm"
        now = datetime.now()

        current_time=now.strftime("%I:%M:%S:%P")
        print("TIME : " + current_time)
        current_date=now.strftime("%d-%m-%Y")
        print("DATE : " + current_date)
        s1 = now.strptime("04:08:30:pm")
        s2 = now.strptime()
        if (current_time<s2):
            print("full")
            #full_night()
        elif (current_time<s1):
            print("day")

            #day_shift()          
        elif (current_time==HALF):
            print("half")

            #half_night()
        time.sleep(1)
