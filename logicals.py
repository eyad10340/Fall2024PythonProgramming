

#variables
jump_1 = 0.0
jump_2 = 0.0
jump_3 = 0.0
jump_4 = 0.0
jump_5 = 0.0
average_of_jumps = 0.0

#input

jump_1 = float(input("Enter the distance in meters of jump 1: "))

jump_2 = float(input("Enter the distance in meters of jump 2: "))

jump_3 = float(input("Enter the distance in meters of jump 3: "))

jump_4 = float(input("Enter the distance in meters of jump 4: "))

jump_5 = float(input("Enter the distance in meters of jump 5: "))

#calculation for average of jumps
average_of_jumps = (jump_1 + jump_2 + jump_3 + jump_4 + jump_5) / 5.0

#print statements
print("The average of the 5 jumps is", format(average_of_jumps, ".2f"))


#if/else statements


if average_of_jumps > 20:
    print("you are disqualified for steroids")
elif average_of_jumps >= 8:
    print("Congrats, you have qualified for the olympics!")
elif average_of_jumps < 3:
    print("Tf are you doing here")
else: 
    print("You have not qualified")