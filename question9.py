# Write a func that takes 3 args:
# from_date - string representing a date in the form of 'yy-mm-dd'
# to_date - string representing a date in the form of 'yy-mm-dd'
# difference - int
# Returns True if from_date and to_date are less than difference days away from each other, else returns False.

# datetime is one of the module used to work with dates and times in python
from datetime import datetime

def check_difference(from_date_str, to_date_str, difference):
    format = "%y-%m-%d"
    from_date = ""
    to_date = ""

    try:
        from_date = datetime.strptime(from_date_str, format).date()
        to_date = datetime.strptime(to_date_str, format).date()
    except:
        print("The input date format is wrong or provided dates are invalid. Exiting...")
        exit(1)

    if(to_date < from_date):
        print("To date should be ahead of from date. Exiting...")
        exit(1)

    days_diff = (to_date - from_date).days

    return days_diff < difference


from_date_str = input("Enter the FROM date in yy-mm-dd format: ")
to_date_str = input("Enter the TO date in yy-mm-dd format: ")
difference = 0
try: 
    difference = int(input("Enter the difference between the dates: "))
except:
    print("Provided an invalid value for difference. Exiting...")
    exit(1)

print("The difference condition gives: ", check_difference(from_date_str, to_date_str, difference))