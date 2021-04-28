
from datetime import datetime

def Main():
    print("Hello. What is your name?")
    name = input("Name: ")
    print(f"Ok {name}. Tell me your birthday and i will tell you how many days since your birthday")
    birth_day = int(input("day: "))
    birth_month = int(input("month: "))
    birth_year = int(input("year: "))
    birth = datetime(birth_year, birth_month, birth_day)
    today = datetime.today()
    days_between = days_between_years(birth.year, today.year)
    days_upto_today = days_upto_a_date(today.day, today.month, today.year) - 1
    days_upto_birth_day = days_upto_a_date(birth.day, birth.month, birth.year) -1
    days_from_birth_year = days_in_the_year(birth.year) - days_upto_birth_day
    total_days = days_between + days_upto_today + days_from_birth_year
    print(f"You have been alive for {total_days} days. Wow.")

def days_in_the_year(year):
    days = 0
    if ( ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0) ):
        return 366
    else:
        return 365

def days_between_years(starting_year, final_year):
    years_apart = final_year - starting_year - 1
    year = starting_year + 1
    days = 0
    for i in range(years_apart):
        days += days_in_the_year(year)
        print(days_in_the_year(year))
        year += 1
    return days

def days_upto_a_date(day, month, year):
    days_upto = 0
    days_with_31_days = {1, 3, 5, 7, 8, 10, 12}
    days_with_30_days = {4, 6, 9, 11}
    start_month = 1
    for i in range(month-1):
        if start_month == 2:
            if ( ( (year % 4 == 0) and (year % 100 == 0) ) or (year % 400 == 0) ):
                days_upto += 29
            else:
                days_upto += 28
        elif start_month in days_with_31_days:
            days_upto += 31
        elif start_month in days_with_30_days:
            days_upto += 30
        start_month += 1
    days_upto += day;
    return days_upto

Main()
