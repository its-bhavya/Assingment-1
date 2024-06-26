#program that asks the user for their birth year and calculates their age.
import datetime
dob = input("Enter DOB (dd-mm-yyyy): ")
present_day = datetime.date.today()
dob_date = datetime.datetime.strptime(dob, '%d-%m-%Y').date()
age_years  = present_day.year - dob_date.year
age_month = present_day.month - dob_date.month
age_days = present_day.day - dob_date.day
print("Age = ", age_years, "years", age_month, "months", age_days, "days")

