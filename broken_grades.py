# Calculating Grades (ok, let me think about this one)

# Write a program that will average 3 numeric exam grades, return an average test score, a corresponding letter grade, and a message stating whether the student is passing.

# Average	Grade
# 90+	    A
# 80-89	    B
# 70-79	    C
# 60-69	    D
# 0-59	    F

# Exams: 89, 90, 90
# Average: 90
# Grade: A
# Student is passing.

# Exams: 50, 51, 0
# Average: 33
# Grade: F
# Student is failing.

exam_one = int(input("Input exam grade one: "))
#Convert the input to integer.
exam_two = int(input("Input exam grade two: "))

#input is converted to integer and variable is changed from exam_3 to exam_three
exam_three = int(input("Input exam grade three: "))

#coma's missing in list grades
grades = [exam_one, exam_two, exam_three]
sum = 0
for grade in grades: #list variables changed from grade to grades
  sum = sum + grade

#spelling error for variable grades
avg = sum / len(grades)

if avg >= 90:
    letter_grade = "A"
elif avg >= 80 and avg < 90: #colon missing 
    letter_grade = "B"
elif avg > 69 and avg < 80:
    letter_grade = "C" #single quotations changes to double quotations
elif avg >= 69 and avg < 70:#changed the values
    letter_grade = "D"
else: #elif changed to else
    letter_grade = "F"

print(f"Exam: {str(exam_one)}, {str(exam_two)}, {str(exam_three)}")
print("Average: " + str(avg))
print("Grade: " + letter_grade)

if letter_grade == "F": #hyphon in letter-grade changed to _ and 'is' changed to ==
    print("Student is failing.")#Brackets added
else:
    print("Student is passing.")#Brackets added
