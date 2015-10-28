# README

## Weekday Calculator

This was a Programming Prompt from: https://www.reddit.com/r/ProgrammingPrompts/comments/2xo554/easy_calculate_the_day_of_the_week_for_any_given/ 

### [Easy] Calculate the day of the week for any given date
This time, it's going to be an easy prompt.

The task is to calculate the day of the week for any given date in the range March 1900 and February 2100.

Use a programming language of your choice.

The user inputs any date in the above range and the program should calculate the day of the week.

I leave the choice of input format for the date up to you.

The calculation works as follows (I'll use the names year, month, day for the given date):

- First, subtract 1900 from the given year
- Multiply this value with 365
- Add the missing leap days (year - 1900) / 4
- If the year is a leap year, subtract 1 if the month is < 3. (Edit thanks to /u/Philboyd_Studge)
- add the days of the months up to but not including month where February always has 28 days. (Leap years are already accounted for.)
- Add the day
- Take the resulting number modulo 7
- The result is the day of the week (0 = Sunday, 1 = Monday, etc.)

Output the date and the day of the week in textual form.
Have fun coding!

### HOWTO

Simply run calculate_weekday.py
It will ask you for the date (input needs to be between March 1900 and February 2100)
The script will return the weekday of that given date