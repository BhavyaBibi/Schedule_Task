from http.client import REQUESTED_RANGE_NOT_SATISFIABLE
from urllib import request
import schedule
import time
import requests
url ="http://codeforces.com/api/contest.list"
page =request.get(url)
data =page.json()

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