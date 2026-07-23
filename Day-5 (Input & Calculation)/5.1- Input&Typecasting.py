# 5.1 - Input
# Input function is used to take input from the user.



name = input("Enter your name: ")
print("Hello, " + name + "! Welcome to the program.")

'''
age = input("Enter your age: ")

age = age + 5

when  using operator + with string and integer, it will give an error. 
So we need to convert the age to integer before adding 5.'''

# solve the error by converting age to integer that is called type casting.
#Type casting -




age = int (input("Enter your age: "))
age = age + 5
print("Your age is:", age)




temprature = input("Enter the today's temprature: ")
print(type(temprature)) 

# it will give string type because input function always return string type.

temprature = float(input("Enter the today's temprature: "))
print(type(temprature)) 
print("Today's temprature is:", temprature)



#convert number to string using str() function.

sales =  50000
text = "The total sales is: " + str(sales)
print(text)
