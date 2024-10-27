#This program calculates whether an employee gets a bonus and how much the bonus will be.
#Author: Eyad Abdilghanie 
#10/27/2024

#Constants
FIVE_UNITS_OR_FEWER = 500
FIVE_HUNDRED_TO_TWOK = 1000
TWO_THOUSAND_TO_FIVEK= 2000
FIVEK_PLUS = 4000

#Variables
bonus = 0
units_sold_this_year = 0
units_sold_last_year = 0
difference= 0

#input statements
units_sold_this_year = int(input("How many units did you sell this year?: "))
units_sold_last_year = int(input("How many units did you sell last year?: "))
difference = units_sold_this_year- units_sold_last_year
#selection structure
if difference > 0:
    # Gets a bonus!
    if difference <= 500:
        bonus = 500
    elif difference > 500 and difference <= 2000:
        bonus = 1000
    elif difference > 2001 and difference <= 5000:
        bonus = 2000
    elif difference > 5000:
        bonus = 4000
    print("Congratulations you have qualified for a bonus!")
    print("Based upon your preformance you increased your units sold by: ", difference)
    print("Your bonus amount is: $", bonus)
else:
    # Did not qualify!
    print("You did not increase your sales this year so you did not qualify.")


#end statment
input("\n press the enter key to exit.")


