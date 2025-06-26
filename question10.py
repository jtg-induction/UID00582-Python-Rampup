# Write a func that takes 2 args:
# date - string representing a date in the form of 'yy-mm-dd'
# n - integer
# Returns the string representation of date n days before 'date'
# E.g. f('16-12-10', 11) should return '16-11-29'

from datetime import timedelta, datetime

def get_date(date, n):
    format = '%y-%m-%d'
    
    actual_date = ""

    try:
        actual_date = datetime.strptime(date, format).date()
    except:
        print('Input format for date is invalid or the date does not exists. Exiting...')
        exit(1)

    date_before_n = actual_date - timedelta(days=n)
    return datetime.strftime(date_before_n, format)


date = input("Enter the date in yy-mm-dd format: ")
n = 0
try:
    n = int(input("Enter the number of days before which the date is required: "))
except:
    print("Please provide a valid input for n")
    exit(1)

print(f"Date before {n} days from {date} will be: {get_date(date, n)}")