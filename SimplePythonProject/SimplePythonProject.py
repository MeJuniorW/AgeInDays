from datetime import datetime

print("Hello. What is your name?")
name = input("Name: ")
print(f"Ok {name}. Tell your birthday and i will tell you how long you have been alive.")
birth_day = int(input("day: "))
birth_month = int(input("month: "))
birth_year = int(input("year: "))
birth_day_full = datetime(birth_year, birth_month, birth_day)
print(f"{birth_day_full.day} / {birth_day_full.month} / {birth_day_full.year}")
today = datetime.today()
print(f"{today.day} / {today.month} / {today.year}")
