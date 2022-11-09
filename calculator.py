#-------------------------------------------------------------------------------
# Name:        module3
# Purpose:
#
# Author:      Nikhil kumar sah
#
# Created:     28-08-2022
# Copyright:   (c) RITIKA SAH 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------
first_number = input("Enter the first number : ")
second_number = input("Enter the second number :")


first_number = int(first_number)
second_number = int(second_number)
print("---------------press any key for operator(+,-,*,%,/) -------")
operator = input("Enter the operator :")

if operator == "+" :
    print(first_number + second_number)

elif operator == "-" :
    print(first_number - second_number)

elif operator == "*" :
    print(first_number * second_number)

elif operator == "%" :
    print(first_number % second_number)

elif operator == "/" :
    print(first_number / second_number)

else :
    print("You are putting an invalid input")
