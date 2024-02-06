"""
Project for Week 4 of "Python Programming Essentials".
Collection of functions to process dates.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

import datetime

def days_in_month(year, month):
    """
    Inputs:
      year  - an integer between datetime.MINYEAR and datetime.MAXYEAR
              representing the year
      month - an integer between 1 and 12 representing the month

    Returns:
      The number of days in the input month.
    """
    if month == 12:																#when the month is 12
        delta_days = 31
    else:																		#when the month is not 12
        date_next_first = datetime.date(year, month+1, 1)
        date_current_first = datetime.date(year, month, 1)
        delta_days = (date_next_first - date_current_first).days				#the difference of days
    return delta_days



def is_valid_date(year, month, day):
    """
    Inputs:
      year  - an integer representing the year
      month - an integer representing the month
      day   - an integer representing the day

    Returns:
      True if year-month-day is a valid date and
      False otherwise
    """  
    if datetime.MAXYEAR >= year >= datetime.MINYEAR:					#year validity
        if 12 >= month >= 1:											#month validity
            if 1 <= day <= days_in_month(year, month):					#day validity
                return True
    return False



def days_between(year1, month1, day1, year2, month2, day2):
    """
    Inputs:
      year1  - an integer representing the year of the first date
      month1 - an integer representing the month of the first date
      day1   - an integer representing the day of the first date
      year2  - an integer representing the year of the second date
      month2 - an integer representing the month of the second date
      day2   - an integer representing the day of the second date

    Returns:
      The number of days from the first date to the second date.
      Returns 0 if either date is invalid or the second date is
      before the first date.
    """
    if is_valid_date(year1, month1, day1) and is_valid_date(year2, month2, day2):  #date validity
        date1 = datetime.date(year1, month1, day1)
        date2 = datetime.date(year2, month2, day2)
        if date2 > date1:													   	   #order validity
            return (date2 - date1).days
    return 0



def age_in_days(year, month, day):
    """
    Inputs:
      year  - an integer representing the birthday year
      month - an integer representing the birthday month
      day   - an integer representing the birthday day

    Returns:
      The age of a person with the input birthday as of today.
      Returns 0 if the input date is invalid or if the input
      date is in the future.
    """

    todays_date = datetime.date.today()
    if is_valid_date(year, month, day) is False:				   	  			    #date invalidity
        return 0
    else:
        birth_date = datetime.date(year, month, day)
        if birth_date > todays_date:	   	  			 							#order invalidity
            return 0
        age = (todays_date - birth_date).days
        return age
    

#this is for testing
#function1
print(days_in_month(2021, 12) == 31)
print(days_in_month(2000, 2) == 29)
print(days_in_month(2001, 2) == 28)
print(days_in_month(2100, 2) == 28)
#funtion2
print("-----------------------------")
print(is_valid_date(2000, 2, 29))
print(is_valid_date(1998, 1, 25))
print(is_valid_date(2000, 2, 30))
print(is_valid_date(2000, 13, 29))
print(is_valid_date(2000, 0, 29))
print(is_valid_date(10000, 2, 21))
print(is_valid_date(1, 2, 21))
#funtion3
print("-----------------------------")
print(days_between(2021, 1, 1, 2022, 1, 1) == 365)
print(days_between(2021, 1, 1, 2021, 1, 2) == 1)
print(days_between(2021, 1, 1, 2021, 1, 1) == 0)
print(days_between(2021, 1, 1, 2020, 12, 31) == 0)
print(days_between(2021, 1, 1, 2021, 1, 1) == 0)
print(days_between(2021, 13, 1, 2020, 12, 31) == 0)
print(days_between(2021, 2, 1, 2022, 2, 29) == 0)
#funtion4
print("-----------------------------")
print(age_in_days(2024, 2, 7) == 0)
print(age_in_days(2021, 2, 30) == 0)
print(age_in_days(2026, 2, 5) == 0)
print(age_in_days(2016, 2, 5) == 0)
print(age_in_days(1999, 2, 29) == 0)
print(age_in_days(1999, 2, 9))