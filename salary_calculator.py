basic=int(input("Enter Your Basic Salary: "))
hra= basic * 0.20
print("Your HRA is: ", hra)
tax= basic * 0.10
print("Your Tax is: ", tax)
in_hand_salary = basic + hra - tax
print("Your In Hand Salary is: ", in_hand_salary)
print("Your Final Salary is: ", in_hand_salary)
