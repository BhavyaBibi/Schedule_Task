from http.client import REQUESTED_RANGE_NOT_SATISFIABLE
import schedule
import time
import requests

def job():
    print("im working")
def coding():
    print("im coding")
def playing():
    print("im playing")


schedule.every(5).seconds.do(job) 
schedule.every(15).seconds.do(coding)  
schedule.every().day.at("11:22").do(playing)

while True:
    schedule.run_pending()
    time.sleep(1)