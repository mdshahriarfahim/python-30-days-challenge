# #Assignment: Salary Slip Calculator


'''
"create a python program to generate an employee salary slip"
write a program that asks the user to enter -
- Employee Name
- Basic Salary
- Bonus Amount
- Tax Percentage
'''

'''


# Hints 
Your program should calculate the following:
- Gross Salary = Basic Salary + Bonus Amount
- Tax Amount = (Gross Salary * Tax Percentage) / 100
- Net Salary = Gross Salary - Tax Amount

Finally, print a clean and clear Salary Slip showing all the values.

'''

# Solve -

employee_name = input("Enter employee name: ")
basic_salary = float(input("Enter basic salary: "))
bonus_amount = float(input("Enter bonus amount: "))
tax_percentage = float(input("Enter tax percentage: "))

gross_salary = basic_salary + bonus_amount
tax_amount = (gross_salary * tax_percentage) / 100
net_salary = gross_salary - tax_amount

print("\n-------Salary Slip-------")
print("Employee Name: ", employee_name)
print("Gross Salary: ", gross_salary)
print("Tax Amount: ", tax_amount)
print("Net Salary: ", net_salary)