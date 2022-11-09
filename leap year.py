#-------------------------------------------------------------------------------
# Name:        NIKHIL KUMAR SAH
# Purpose:     IDENTIFYING A LEAP YEAR
#
# Author:      NIKHIL KUMAR SAH
#
# Created:     09-09-2022
# Copyright:   (c) NIKHIL KR. SAH 2022
# Licence:     <Trom's licence>
#-------------------------------------------------------------------------------

'''Year = int(input("Enter the year:"))

if(int(Year%4 ==0)):
    print(int(Year),"is a leap year")

else:
    print("it is not a leap year")'''


year = int(input('Enter year:'))

if(year%4 == 0 and year%100 != 0) or (year%400 == 0):
    print(year, "is a leap year.")
else:
    print(year,"is not a leap year.")


