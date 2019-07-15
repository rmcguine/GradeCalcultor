#Ask for exam grade inputs out of 100
exam1_grade = float(input('Enter score on Exam 1 (out of 100):\n'))
exam2_grade = float(input('Enter score on Exam 2 (out of 100):\n'))
exam3_grade = float(input('Enter score on Exam 3 (out of 100):\n'))

#Calculate exam grade percentages
exam1 = exam1_grade / 100 * 100
exam2 = exam2_grade / 100 * 100
exam3 = exam3_grade / 100 * 100

#Calculate exam grade averages
avg_exam_grade = (exam1 + exam2 + exam3) / 3

#Ask for programming grade inputs out of 50
pro1_grade = float(input('Enter score on Program 1 (out of 50):\n'))
pro2_grade = float(input('Enter score on Program 2 (out of 50):\n'))
pro3_grade = float(input('Enter score on Program 3 (out of 50):\n'))
pro4_grade = float(input('Enter score on Program 4 (out of 50):\n'))

#Calculate programming grade percentages
pro1 = pro1_grade / 50 * 100
pro2 = pro2_grade / 50 * 100
pro3 = pro3_grade / 50 * 100
pro4 = pro4_grade / 50 * 100

#Calculate exam grade averages
avg_pro_grade = (pro1 + pro2 + pro3 + pro4) / 4

#Calculate Assignment Account Distribution; Exam 60% of grade; Pro 40% of grade
final_grade = float((avg_exam_grade * .6) + (avg_pro_grade * .4))

#Print final grade
print('Your overall grade is:', final_grade)
