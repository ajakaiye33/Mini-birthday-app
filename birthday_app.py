#birthday app

from datetime import datetime
def print_header():
    print("----------------------------------")
    print("               Birthday App")
    print("----------------------------------")


# ask/collect the birthday details from user
def user_birth_details():
    name = input('what is your name? ')
    greeting = print('Hey {}, whatup, lets have some your birthday details'.format(name.upper()))
    year = int(input('What year were you born [YYYY]? '))
    month = int(input('What month were you born [MM]? '))
    day = int(input('What day were you born[DD]? '))


    bday_in_datetime = datetime(year, month, day)
    return bday_in_datetime

    #To get the number of days before your birthday or the number of days past your birthday

def compute_days_to_bday(orig_birthday, birthday_this_yr):
    # derive the birth day for this year

    this_yr = datetime(birthday_this_yr.year, orig_birthday.month, orig_birthday.day)
    checkgar = this_yr - birthday_this_yr
    return checkgar.days

# Display the number of days after your birthday  or number of days before your bithday
def display_result(dayz):
    if dayz < 0:
        print('Your birthday was {} days ago'.format(-dayz))
    elif dayz > 0:
        print('Your birthday is in {} days time'.format(dayz))
    else:
        print('Happy birthday congratulations')






def main():
    print_header()
    details = user_birth_details()
    now_date = datetime.today()
    thecal_days = compute_days_to_bday(details,now_date)
    display_result(thecal_days)




main()
