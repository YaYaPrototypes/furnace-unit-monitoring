import time
from datetime import datetime
while True:
    hour=str(input("number : "))

    full=["0","1","2","3","4","5","6","7"]
    day=["8","9","10","11","12","13","14","15","16"]
    half=["17","18","19","20","21","22","23"]
         
    if hour in day:
        print("day")
    elif hour in half:
        print("half")
    elif hour in full:
        print("full")