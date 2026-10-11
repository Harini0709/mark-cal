name = "Harini"
python = 85
sql = 90
machine_learning = 80

total = python + sql + machine_learning
average = total / 3

print("STUDENT MARKS REPORT")
print("Name:", name)
print("Python:", python)
print("SQL:", sql)
print("Machine Learning:", machine_learning)
print("Total:", total, "/ 300")
print("Average:", average)

if average >= 50:
    print("Result: PASS")
else:
    print("Result: FAIL")
