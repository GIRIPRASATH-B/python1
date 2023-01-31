#2 PROGRAM
grade = input("Enter the grade of the employee: ")
salary = float(input("Enter the employee salary: "))
if grade.upper() =='B'  and salary==0:
    print("enter valid salary")
elif grade.upper() == 'A' and salary >= 10000:
    bonus = salary * 0.05
    total_salary = salary + bonus
    print("Salary=",salary)
    print("Bonus=",bonus)
    print("Total to be paid:",total_salary)
elif grade.upper() == 'A' and salary < 10000:
    bonus = salary * 0.07
    total_salary = salary + bonus
    print("Salary=",salary)
    print("Bonus=",bonus)
    print("Total to be paid:",total_salary)
elif grade.upper() == 'B' and salary >= 10000:
    bonus = salary * 0.1
    total_salary = salary + bonus
    print("Salary=",salary)
    print("Bonus=",bonus)
    print("Total to be paid:",total_salary)
elif grade.upper() == 'B' and salary < 10000:
    bonus = salary * 0.12
    total_salary = salary + bonus
    print("Salary=",salary)
    print("Bonus=",bonus)
    print("Total to be paid:",total_salary)
else:
    print("Invalid input")
