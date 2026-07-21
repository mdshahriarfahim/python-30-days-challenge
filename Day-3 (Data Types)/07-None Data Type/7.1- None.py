# 7.1 - None data type

x = None
print(x)
print(type(x))


remarks = None
print(remarks)
print(type(remarks))


result = 10 + None
print(result)  #output: TypeError: unsupported operand type(s) for +: 'int' and 'NoneType'
print(type(result))  #output: TypeError: unsupported operand type(s) for +: 'int' and 'NoneType'