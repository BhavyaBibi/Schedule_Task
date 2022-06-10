import schedule
import time

def job():
    print("im working")
def coding():
    print("im coding")

schedule.every(5).minutes.do(job) 
schedule.every(15).minutes.do(coding)  

while True:
    schedule.run_pending()
    time.sleep(1)