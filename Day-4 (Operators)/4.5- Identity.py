# 4.5 -Identity Operators


'''

is - Returns True if both variables are the same object     (x is y)
is not - Returns True if both variables are not the same object (x is not y)

'''



m1 = 10
m2 = 10
m3 = 20

print(m1 is m2)      # Output: True
print(m1 is not m3)  # Output: True

'''
comment: The 'is' operator checks if two variables point to the same object in memory,
while 'is not' checks if they do not point to the same object. In this example,
m1 and m2 are both assigned the value 10, so they refer to the same object in memory,
resulting in True for 'm1 is m2'. On the other hand, m1 and m3 have different values (10 and 20)
, so 'm1 is not m3' returns True.  


comment: It's important to note that 'is' and 'is not' are identity operators, 
which means they compare the memory addresses of the objects, not their values.
For value comparison, you would use the equality operator '==' instead.

'''

