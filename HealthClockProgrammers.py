# https://www.geeksforgeeks.org/create-health-clock-for-programmers-using-python/?ref=rp
# import required modules
# from pygame import mixer
from time import time
from time import sleep
import schedule
  
def getdate():
 
    # To get the current date and time
    # at time of entry
    import datetime
    return (str(datetime.datetime.now())) 
 
def musicloop(stopper):
    # mixer.init()
    # mixer.music.load("music.mp3")
 
    # playing the music provided i.e. music.mp3
    # mixer.music.play()
    while True:
        x = input(
            "Please type STOP to stop the alarm or EXIT to stop the program : ")
 
        # music termination condition.
        if (x.upper() == stopper):
            print("\nGreat! Get back to work:)\n")
            # mixer.music.stop()
            return True
            # break
 
        # program termination condition.
        elif (x.upper() == "EXIT"):
            return False
 
def printTimeVal():
    # print(time() - oriTime, ' has passed.')
    print('2 seconds have passed.')
 
# variables initialized with 0 for counting total
# number of exercises and water drank in a day
total_water = 0
total_physical_exercises = 0
total_eye_exercises = 0
 
if __name__ == '__main__':
    print("\n\t\t\t\tHey Programmer! This is your Health-Alarm-Clock\n")
    time_phy = time()
    time_drink = time()
    time_eyes = time()
 
    eyes_delay = 10
    drink_delay = 20
    phy_delay = 35
    schedule.every(2).seconds.do(printTimeVal)
    
    while(True):
        schedule.run_pending()
        # Drink water condition.
        if (time() - time_drink > drink_delay):
            print(">>>>>>>>>>>>>>> Hey! Please drink some water (at least 200 ml).")
 
            # Checking the user input so that music
            # can be stopped.
            if(musicloop("STOP")):
                pass
            else:
                break
 
            # reinitializing the variable
            time_drink = time()
 
            # incrementing the value
            total_water += 200
            print('Total water is now: ', total_water)
 
            # opening the file and putting the data
            # into that file
            f = open("drank.txt", "at")
            f.write("\n [ " + getdate() + " ] :" + str(total_water) + ' mL')
            f.close()
 
        # Eye exercise condition.
        if (time() - time_eyes > eyes_delay):
 
            print(">>>>>>>>>>>>>>> Hey! Please do an Eye Exercise.")
 
            if (musicloop("STOP")):
                pass
            else:
                break
 
            time_eyes = time()
            total_eye_exercises += 1
            print('Total eye exercises is now: ', total_eye_exercises)
            f = open("eye.txt", "at")
            f.write("\n [ " + getdate() + " ]: " + str(total_eye_exercises))
            f.close()
 
        # Eye exercise condition.
        if (time() - time_phy > phy_delay):
            print(">>>>>>>>>>>>>>> Hey! Please do a Physical Exercise.")
 
            if (musicloop("STOP")):
                pass
            else:
                break
 
            time_phy = time()
            total_physical_exercises += 1
            print('Total physical exercise is now: ', total_physical_exercises)
            f = open("phy_exer.txt", "at")
            f.write("\n [ " + getdate() + " ]: " + str(total_physical_exercises))
            f.close()
    schedule.clear()

    print()
    print(f"Total water taken today : {total_water}.")
 
    try:
        f = open("drank.txt", "rt")
        print("\nDetails :")
        print(f.read())
        f.close()
    except:
        print("Details not found!")
 
    print(f"Total eye exercise done today : {total_eye_exercises}.")
 
    try:
        f = open("eye.txt", "rt")
        print("\nDetails :")
        print(f.read())
        f.close()
    except:
        print("Details not found!")
 
    print(f"Total physical exercises done today : {total_physical_exercises}.")
 
    try:
        f = open("phy_exer.txt", "rt")
        print("\nDetails :")
        print(f.read())
        f.close()
    except:
        print("Details not found!")
 
    sleep(5)

# https://www.geeksforgeeks.org/python-schedule-library/
# Schedule Library imported
import schedule
import time
 
# Functions setup
def sudo_placement():
    print("Get ready for Sudo Placement at Geeksforgeeks")
 
def good_luck():
    print("Good Luck for Test")
 
def work():
    print("Study and work hard")
 
def bedtime():
    print("It is bed time go rest")
     
def geeks():
    print("Shaurya says Geeksforgeeks")
 
# Task scheduling
# After every 10mins geeks() is called.
schedule.every(10).minutes.do(geeks)
 
# After every hour geeks() is called.
schedule.every().hour.do(geeks)
 
# Every day at 12am or 00:00 time bedtime() is called.
schedule.every().day.at("00:00").do(bedtime)
 
# After every 5 to 10mins in between run work()
schedule.every(5).to(10).minutes.do(work)
 
# Every monday good_luck() is called
schedule.every().monday.do(good_luck)
 
# Every tuesday at 18:00 sudo_placement() is called
schedule.every().tuesday.at("18:00").do(sudo_placement)

schedule.every(2).seconds.do(printTimeVal) 
# Loop so that the scheduling task
# keeps on running all time.
while True:
    # Checks whether a scheduled task
    # is pending to run or not
    schedule.run_pending()
    time.sleep(1)

    x = input("Please type STOP to stop: ")
    # music termination condition.
    if (x.upper() == "STOP"):
        print("\nGreat! END OF TEST.\n")
        # mixer.music.stop()
        break
    else:
        pass

while (x := input("Please type STOP to stop: ")) != 'STOP':
    # Checks whether a scheduled task
    # is pending to run or not
    schedule.run_pending()
    time.sleep(1)
        
print("\nEND OF TEST.\n")

schedule.clear()
"""
schedule.Scheduler class
schedule.every(interval=1) : Calls every on the default scheduler instance. Schedule a new periodic job.
schedule.run_pending() : Calls run_pending on the default scheduler instance. Run all jobs that are scheduled to run.
schedule.run_all(delay_seconds=0) : Calls run_all on the default scheduler instance. Run all jobs regardless if they are scheduled to run or not.
schedule.idle_seconds() : Calls idle_seconds on the default scheduler instance.
schedule.next_run() : Calls next_run on the default scheduler instance. Datetime when the next job should run.
schedule.cancel_job(job) : Calls cancel_job on the default scheduler instance. Delete a scheduled job.

Basic methods for Schedule.job
 
at(time_str) : Schedule the job every day at a specific time. Calling this is only valid for jobs scheduled to run every N day(s).
Parameters: time_str – A string in XX:YY format. 
Returns: The invoked job instance
do(job_func, *args, **kwargs) : Specifies the job_func that should be called every time the job runs. Any additional arguments are passed on to job_func when the job runs.
Parameters: job_func – The function to be scheduled 
Returns: The invoked job instance
run() : Run the job and immediately reschedule it. 
Returns: The return value returned by the job_func
to(latest) : Schedule the job to run at an irregular (randomized) interval. For example, every(A).to(B).seconds executes the job function every N seconds such that A <= N <= B.
"""

# https://www.geeksforgeeks.org/10-essential-python-tips-tricks-programmers/?ref=rp

test = [1, 2, 3, 4, 2, 2, 3, 1, 4, 4, 4]
print(max(set(test), key = test.count))
# Output: 4