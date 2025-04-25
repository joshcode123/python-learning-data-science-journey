#This allows you to enter students scores and grades

#Ask user number of students to enter
num_of_students = int(input("How many students scores do you want to enter? : "))

student_names = []
student_scores = []

for i in range(num_of_students):
    students = input("Enter students name: ")
    scores = float(input("Enter students scores: "))

    student_names.append(students)
    student_scores.append(scores)


passed_student = 0
failed_student = 0

for i in range(len(student_names)):
    if student_scores[i] >= 90:
        grade = "A"
        print(f"{student_names[i]} scored {student_scores[i]} you have {grade}")
    elif student_scores[i] >=80 :
        grade = "B"
        print(f"{student_names[i]} scored {student_scores[i]} you have {grade}")
    elif student_scores[i] >=70 :
        grade = "C"
        print(f"{student_names[i]} scored {student_scores[i]} you have {grade}")
    elif student_scores[i] >=60 :
        grade = "D"
        print(f"{student_names[i]} scored {student_scores[i]} you have {grade}")
    elif student_scores[i] >= 50:
        grade = "E"
        print(f"{student_names[i]} scored {student_scores[i]} you have {grade}")
    else:
        grade = "F"
        print(f"{student_names[i]} scored {student_scores[i]} you have {grade}")


    if student_scores[i] >= 50 :
        print(f"{student_names[i]} scored{student_scores} you have {grade} PASSED")
        passed_student += 1
    else:
        print(f"{student_names[i]} scored{student_scores} you have {grade} FAILED")
        failed_student += 1


print(f"Number of students that passed {passed_student}")
print(f"Number of students that failed {failed_student}")

average_score = sum(student_scores) / len(student_names)
print(f"Average score is {average_score}")

list_of_passed_students = [student_names[i] for i in range(len(student_names)) if student_scores[i] >= 50]
print(f"Those who passed are: {list_of_passed_students}")