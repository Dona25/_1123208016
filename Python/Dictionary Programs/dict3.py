student = {"Ram": 90,"Sam": 85,"Ravi": 95}
highest = max(student, key=student.get)
print("Top Student:", highest)
print("Marks:", student[highest])