# #birthday app
#
# from datetime import datetime
# def print_header():
#     print("----------------------------------")
#     print("               Birthday App")
#     print("----------------------------------")
#
#
# # ask/collect the birthday details from user
# def user_birth_details():
#     name = input('what is your name? ')
#     greeting = print('Hey {}, whatup, lets have some your birthday details'.format(name.upper()))
#     year = int(input('What year were you born [YYYY]? '))
#     month = int(input('What month were you born [MM]? '))
#     day = int(input('What day were you born[DD]? '))
#
#
#     bday_in_datetime = datetime(year, month, day)
#     return bday_in_datetime
#
#     #To get the number of days before your birthday or the number of days past your birthday
#
# def compute_days_to_bday(orig_birthday, birthday_this_yr):
#     # derive the birth day for this year
#
#     this_yr = datetime(birthday_this_yr.year, orig_birthday.month, orig_birthday.day)
#     checkgar = this_yr - birthday_this_yr
#     return checkgar.days
#
#
# def display_result(dayz):
#     if dayz < 0:
#         print('Your birthday was {} days ago'.format(-dayz))
#     elif dayz > 0:
#         print('Your birthday is in {} days time'.format(dayz))
#     else:
#         print('Happy birthday congratulations')
#
#
#
#
#
#
# def main():
#     print_header()
#     details = user_birth_details()
#     print(details)
#     now_date = datetime.today()
#     thecal_days = compute_days_to_bday(details,now_date)
#     display_result(thecal_days)
#
#
#
#
# main()


'''Extract datetimes from log entries and calculate the time
   between the first and last shutdown events'''
from datetime import datetime
import os
import urllib.request

SHUTDOWN_EVENT = 'Shutdown initiated'

# prep: read in the logfile
logfile = os.path.join('/tmp', 'log')
urllib.request.urlretrieve('http://bit.ly/2AKSIbf', logfile)

with open(logfile) as f:
    loglines = f.readlines()


# for you to code:

def convert_to_datetime(line):
    '''TODO 1:
       Given a log line extract its timestamp and convert it to a datetime object.
       For example calling the function with:
       INFO 2014-07-03T23:27:51 supybot Shutdown complete.
       returns:
       datetime(2014, 7, 3, 23, 27, 51)'''
    sert = ""
    for i in line:
        sert += i



    return sert.split('\n')[1]


print(convert_to_datetime(loglines))


#
# def time_between_shutdowns(loglines):
#     '''TODO 2:
#        Extract shutdown events ("Shutdown initiated") from loglines and calculate the
#        timedelta between the first and last one.
#        Return this datetime.timedelta object.'''
#     pass
