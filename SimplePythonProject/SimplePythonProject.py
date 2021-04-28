
from datetime import datetime

def Main():
    print("Hello. What is your name?")
    name = input("Name: ")
    print(f"Ok {name}. Tell me your birthday and i will tell you how many days since your birthday")
    birth_day = int(input("day: "))
    birth_month = int(input("month: "))
    birth_year = int(input("year: "))
    birth_day_full = datetime(birth_year)
    today = datetime.today()
    years_apart = today.year - birth_day_full.year
    year = birth_day_full.year
    print(today.year)


def days_in_the_year(year):
    days = 0
    if ( ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0) ):
        return 365
    else:
        return 364

def days_apart_years(starting_year, final_year):
    years_apart = final_year - starting_year
    year = starting_year
    days = 0
    for i in range(years_apart):
        days = days + days_in_the_year(year)
        year += 1
    return days

def days_upto_a_date(day, month, year):
    days_upto = 0
    days_with_31_days = {1, 3, 5, 7, 8, 10, 12}
    for i in range(month+1):
        if month == 2:
            if ( ( (year % 4 == 0) and (year % 100 == 0) ) or (year % 400 == 0) ):
                days_upto = days_upto + 29
            else:
                days_upto = days_upto + 28
        elif month in days_with_30_days:
            days_upto = days_upto + 30
        else:
            days_upto = days_upto + 31
    days_upto = days_upto - day - 1;
    return days_upto

Main()
