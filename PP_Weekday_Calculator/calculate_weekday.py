"""The task is to calculate the day of the week for any given date in the range March 1900 and February 2100.

Use a programming language of your choice.

The user inputs any date in the above range and the program should calculate the day of the week.

I leave the choice of input format for the date up to you.

The calculation works as follows (I'll use the names year, month, day for the given date):

    First, subtract 1900 from the given year
    Multiply this value with 365
    Add the missing leap days (year - 1900) / 4
    If the year is a leap year, subtract 1 if the month is < 3. (Edit thanks to /u/Philboyd_Studge)
    add the days of the months up to but not including month where February always has 28 days. (Leap years are already accounted for.)
    Add the day
    Take the resulting number modulo 7
    The result is the day of the week (0 = Sunday, 1 = Monday, etc.)

Output the date and the day of the week in textual form."""

input_date = raw_input("Please insert date (dd-mm-yyyy): ")

day = int(input_date[0:2])
month = int(input_date[3:5])
year =  int(input_date[6:10])
days_per_year = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
week_day = {0:"Sunday", 1:"Monday", 2:"Tuesday", 3:"Wednesday", 4:"Thursday", 5:"Friday", 6:"Saturday"}


x = year - 1900
total_days = 365 * x
total_days += x/4
if year%4 == 0 and month < 3:
	total_days += - 1
for i in days_per_year[0:month-1]:
	total_days += i
total_days += day
print week_day[total_days % 7]