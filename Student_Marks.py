marks = []

for i in range(5):
    mark = float(input("Enter marks for subject " + str(i+1) + ": "))
    marks.append(mark)

total = sum(marks)
percentage = total / 5

print("Total Marks:", total)
print("Percentage:", percentage)

if percentage >= 90:
    grade = "A"
elif percentage >= 75:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 40:
    grade = "D"
else:
    grade = "Fail"

print("Grade:", grade)