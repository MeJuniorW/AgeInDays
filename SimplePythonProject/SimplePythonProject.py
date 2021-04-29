
from datetime import datetime

def Main():
    print("Hello. What is your name?")
    name = input("Name: ")
    print(f"Ok {name}. Tell me your birthday and i will tell you how many days since your birthday")
    today = datetime.today()
    while True:
        try:
            birth_day = int(input("day: "))
            birth_month = int(input("month: "))
            birth_year = int(input("year: "))
            if birth_month > 12 or birth_month < 0:
                raise Exception("Not a valid month")
            if (birth_day > days_in_the_month(birth_month, birth_year)):
                raise Exception("Not a valid day")
            if birth_year < 0 or birth_year > today.year:
                raise Exception("Not a valid year")
            break
        except ValueError:
            print("That could not be converted to an integer")
        except Exception as instance:
            x = instance.args
            print(f"{x}")

    birth = datetime(birth_year, birth_month, birth_day)
    
    days_between = days_between_years(birth.year, today.year)
    days_upto_today = days_upto_a_date(today.day, today.month, today.year) - 1
    days_upto_birth_day = days_upto_a_date(birth.day, birth.month, birth.year) -1
    days_from_birth_year = days_in_the_year(birth.year) - days_upto_birth_day
    total_days = days_between + days_upto_today + days_from_birth_year
    print(f"You have been alive for {total_days} days. Wow.")

def days_in_the_year(year):
    if ( ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0) ):
        return 366
    else:
        return 365

def days_in_the_month(month, year):
    days = 0
    days_with_31_days = {1, 3, 5, 7, 8, 10, 12}
    days_with_30_days = {4, 6, 9, 11}
    if month == 2:
        if ( ( (year % 4 == 0) and (year % 100 != 0) ) or (year % 400 == 0) ):
            days = 29
        else:
            days = 28
    elif month in days_with_31_days:
        days = 31
    elif month in days_with_30_days:
        days += 30
    return days

def days_between_years(starting_year, final_year):
    years_apart = final_year - starting_year - 1
    year = starting_year + 1
    days = 0
    for i in range(years_apart):
        days += days_in_the_year(year)
        year += 1
    return days

def days_upto_a_date(day, month, year):
    days_upto = 0
    start_month = 1
    for i in range(month-1):
        days_upto += days_in_the_month(start_month, year)
        start_month += 1
    days_upto += day;
    return days_upto

Main()
