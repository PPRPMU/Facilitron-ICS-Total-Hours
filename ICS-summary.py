import numpy as np
import pandas as pd
import ics
import requests

print('please enter the file path to the data file (on PC replace \ with /):')
fpath = input()
print('please enter the file name used (should be a csv):')
fname = input()
path = fpath+'/'+fname
#path = 'C:/Users/pkeen/OneDrive - City of Philadelphia/automation/SchoolPermits2023.csv'
#load csv file
csvFile = pd.read_csv(path)
#drop nan values
csvFile=csvFile[csvFile['Facilitron-Request-Number'].notna()]
#get all of the unique reservation numbers in the dataset
reservationIDs = csvFile['Facilitron-Request-Number'].unique()
#initialize count variable
totalHours = 0
#loop through all unique reservations and get the ICS file for each
for ireservation in range(len(reservationIDs)):
    thisResID = reservationIDs[ireservation]
    #define url and get ICS file
    url = "https://www.facilitron.com/icalendar/reservation/"+thisResID
    r = requests.get(url,verify=True) #Will not work on City internet
    #load the ics calendar
    c = ics.Calendar(r.text)
    #get a list of every event in the calendar
    eventList = list(c.events)
    #loop through every unique event and total up the number of hours
    for ievent in range(len(eventList)):
        #get duration from calendar in seconds
        eventDurationinSec = eventList[ievent].duration.total_seconds()
        #convert to hours
        eventDurationinHours = (eventDurationinSec/60)/60
        #add to the count variable
        totalHours = totalHours + eventDurationinHours
#return the total number of hours
print(totalHours)    
