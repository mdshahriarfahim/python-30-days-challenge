# 4.4- Logical Operators

'''


and - Returns True if both statements are true     (5 > 3 and 5 < 10 = True)
or  - Returns True if one of the statements is true  (5 > 3 or 5 > 10 = True)
not - Reverse the result, returns False if the result is true (not(5 > 3) = False)

'''


num1 = 10
num2 = 3
print(num1 > 5 and num2 < 5)  # output - True
print(num1 > 5 or num2 > 5)   # output - True
print(not(num1 < 5))           # output - True
print(not(num2 > 5))           # output - True
print(num1 > 5 and num2 > 5)   # output - False




P1 = 200
P2 = 33
p3 = 500
p4 = 1000
print(P1 > P2 and p3 > p4)  # output - False
print(P1 > P2 or p3 > p4)   # output - True
print(not(P1 < P2))           # output - True
print(not(p3 < p4))           # output - True
print(P1 > P2 and p3 > p4)   # output - False
