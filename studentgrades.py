

num_students = 0
scores = []
num_students = int(input("Enter the number of students in the class: "))
print("----------------------------------------------------------------------------------")


#selection struture for grades
grade = " "

for i in range (num_students):
    scores.append(float(input("Enter the score for the student: ")))

for i in range (num_students):   

    if scores[i] >= 90:
        grade = "A"
    elif scores[i] >=80 and scores[i] < 90:
        grade = "B"   
    elif scores[i] >=70 and scores[i] < 80:
        grade = "C"   
    elif scores[i] >=60 and scores[i] < 70:
        grade = "D"  
    else:
        grade = "F"
    print("For student with score", scores[i], "The grade is ", grade)

#exit program
input("\ press the enter key to exit")