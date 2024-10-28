print("~~~~Mini Calculator~~~~")
num1 = float(input("enter first number here: "))
num2 = float
(input("enter secound number here:"))

print ("press 1 for addition \npress 2 for subtracction \npress 3 for multiplication \npress 4 for division ")
choice= int(input("enter your choice from 1-4:"))
if choice == 1:
    print ("the addition of two given numbers",num1 + num2)
elif choice == 2:
    print ("the subtrection of two given numbers is",num1-num2)
elif choice == 3:
    print ("the multiplication of two given numbers is",num1 * num2)
elif choice == 4:
    print ("the division of two given numbers is ",num1 / num2)
else:
    print ("invild input")
