import random

# Welcome message
print("Welcome to the Number Guessing Game!")

# Set the range for the random number
lower_limit = 1
upper_limit = 100

secret_number = random.randint(lower_limit, upper_limit)

# sum=0
# for ey in range(10, 20, 2):
#     print(ey)
#variables
counter = 0
user_guess = 0
flag = False



while flag ==False:
    user_guess = int(input("Take a guess of what the secret number is: "))
    counter = counter + 1
    print("Attemp", counter)
    if user_guess > secret_number:
        print("The number is too high choose another number") 
    elif user_guess < secret_number:
        print("The number is too low choose a bigger number")
    else:
        print("Congratulations!!!!!!! You chose the correct number in only",counter, "attempts")
        print("The secret number is", user_guess)
        flag = True


    