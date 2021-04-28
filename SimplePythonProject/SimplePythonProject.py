from datetime import datetime

def Main():
    print("Hello. What is your name?")
    name = input("Name: ")
    print(f"Ok {name}. Tell your birthday and i will tell you how many days you have lived")
    birth_day = int(input("day: "))
    birth_month = int(input("month: "))
    birth_year = int(input("year: "))
    birth_day_full = datetime(birth_year, birth_month, birth_day)
    today = datetime.today()
    years_apart = today.year - birth_day_full.year
    year = birth_day_full.year


    
def days_in_the_year(year):
    days = 0
    if ( ( (year % 4 == 0) and (year % 100 == 0) ) or (year % 400 == 0) ):
        days = days + 365
    else:
        days = days + 364
    return days

Main()
