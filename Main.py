#!/usr/bin/env python
# This program calculates whether a Martian year is a Martian leap year
# A Martian year is a Martian leap year if it is divisible by 10 or odd

year = "" #set initial value for year variable

while year != "exit":
 year = input("Please enter a Martian year or type exit: ")
 if year.isnumeric():
     year = int(year)
     if year%10 == 0:
         print(year, "is a Martian leap year.")
         print(year, "is divisible by 10.\n")
     elif year%2 != 0:
          print(year, "is a Martian leap year.")
          print(year, "is odd.\n")
     else:
          print(year, "is a not a Martian leap year.")
          print(year, "is both even and not divisible by 10.\n")
else:
                 if year.lower() == "exit":
                     year = year.lower()
                     print("Goodbye.")
                 else:
                     print("I don't understand. Try again.\n")
