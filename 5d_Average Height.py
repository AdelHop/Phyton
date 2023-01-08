student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

studentMax = int(student_heights[0])

for student in student_heights:

  if student > studentMax:
    studentMax = student

print(studentMax)
# print(int(round(sum(student_heights) / (len(student_heights)), 0)))
# print(max(student_heights))
# print(min(student_heights))

# with loop
# a = 0
# b = 0
#
# for student in student_heights:
#   a += student
#   b += 1
#
# print(int(round((a/b), 0)))

