# #  Practice Problem - 2 :
#Discount Price Calculator

item = input("Enter Item Name: ")
price = float(input("Original Price: "))
discount = float(input("Discount Percentage: "))

discount_amount = price * discount / 100
final_price =  price - discount_amount

print("Final Price of ",item , "=", final_price)

