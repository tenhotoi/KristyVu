# https://www.w3schools.com/python/python_datetime.asp

from datetime import datetime

x = datetime.now()
print(x)

print(x.year)
print(x.strftime("%A"))

y = datetime(2020, 12, 17)

print(y)
print(y.strftime("%B"))

"""
Output:
2023-03-12 12:59:18.876263
2023
Sunday
2020-12-17 00:00:00
December
"""


format_codes = ['a', 'A', 'w', 'd', 'b', 'B', 'm', 'y', 'Y', 'H', 'I', 'p', 'M', 'S', 'f', 'z', 'Z', 'j', 'U', 'W', 'c', 'C', 'x', 'X', r'%', 'G', 'u', 'V']
for each in format_codes:
    print("\n Trying one of the legal format codes: \n", each, x.strftime("%"+each))

timelapse = x - y
print(timelapse)
print(timelapse.days)
print(timelapse.max)
print(timelapse.min)

def diff_month(d1, d2):
    return (d1.year - d2.year) * 12 + d1.month - d2.month

assert diff_month(datetime(2010,10,1), datetime(2010,9,1)) == 1
assert diff_month(datetime(2010,10,1), datetime(2009,10,1)) == 12
assert diff_month(datetime(2010,10,1), datetime(2009,11,1)) == 11
assert diff_month(datetime(2010,10,1), datetime(2009,8,1)) == 14

print('Number of months between the 2 dates:', diff_month(x, y))

"""
https://www.techtarget.com/searchsoftwarequality/tip/How-to-write-a-good-user-story-for-cleaner-code

User workflow.  Always keep the end user in mind. In the user workflow section, development teams should incorporate design discussion elements and add specific details of the anticipated user workflow, so they aren't missed during the design phase.

Let's revisit our medical support application example. If we want to add a feature to an application for a patient to record medication doses and order refills, the user story needs to outline the expected workflow. For example:

Patients fill out the form to sign up for the Medication Management Program through their medical provider.
Patient receives the Consent form, signs it and returns it electronically.
The Medication Management Program reviews the patient and accepts or denies their participation.
If accepted, the patient receives a welcome email or letter and call from a Patient Program Manager.
The patient receives their initial fulfillment of the medication.
The patient records dose intake for 3 months.
The patient reviews their medical records for accuracy. They check appointments they’ve attended and any results from those appointments.
If denied, the patient receives an email or letter indicating they are ineligible for the program.
Once the patient reaches the last 30 days of the three-month program, they automatically receive a refill.
The refill is sent Second Day air and requires the patient's signature.
The refill includes a patient-specific barcode.
The patient receives their refill and uploads the barcode.
The patient continues to track dose intake for the next 3 months.
The patient reviews their medical record for accuracy.
The cycle repeats so long as the patient remains active in the Medication Management Program.
When you add details to the user workflow, it ensures the designed code and testing efforts verify the workflow items are met. In other words, when the user receives your code release, they can perform the user workflow steps as expected.
"""
# https://www.geeksforgeeks.org/python-schedule-library/
# https://schedule.readthedocs.io/en/stable/

"""
# Sample: Schedule every 1st day of the month:
# The main contributor of the library discourages this sort of thing, see https://github.com/dbader/schedule/issues/73#issuecomment-167758653.
# Yet, if one insists, one can schedule a daily job but run it only if it's the 1st of the month.
from datetime import date

from safe_schedule import SafeScheduler


def job2():
    if date.today().day != 1:
        return

    # actual job body


scheduler = SafeScheduler()
scheduler.every().day.at("02:00").do(job2)

# https://schedule.readthedocs.io/en/stable/examples.html#run-a-job-once
# Run a job once
# Return schedule.CancelJob from a job to remove it from the scheduler.


def job_that_executes_once():
    # Do some work that only needs to happen once...
    return schedule.CancelJob

schedule.every().day.at('22:30').do(job_that_executes_once)

while True:
    schedule.run_pending()
    time.sleep(1)

import schedule
from datetime import date
"""
import schedule

def schedule_3months(d):
    date3months = d.month + 3
    return d.year, date3months, d.day

def job(datevar, monthvar, yearvar): 
    if datetime.today().day != datevar or datetime.today().month != monthvar or datetime.today().year != yearvar:
        return

    # actual job body
    # Do some work that only needs to happen once...
    return schedule.CancelJob

# schedule.every().day.at("02:00").do(job)


# MY TRYING:

def sign_up():
    date = datetime.now()

yearvar, monthvar, datevar = schedule_3months(datetime.now())
print(datetime(yearvar, monthvar, datevar))  
print(datetime.today()) 
print(datetime.now())

# Cancel all jobs
# To remove all jobs from the scheduler, use schedule.clear()

import schedule

def greet(name):
    print('Hello {}'.format(name))

schedule.every().second.do(greet)

schedule.clear()
    


    