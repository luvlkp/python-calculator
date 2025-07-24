# Add
# Subtract
# Multiply
# Divide
while True:
  print("1. Addition")
  print("2. Subtraction")
  print("3. Multiplication")
  print("4. Division")
  operation = input("What operation would you like to use? ")
  
  
  
  if int(operation) == 1:
    num1= input("Enter the first number: ")
    num2= input("Enter the second number: ")
    print("Your sum is " + str(int(num1)+int(num2)))
  elif int(operation) == 2:
    num1= input("Enter the first number: ")
    num2= input("Enter the second number: ")
    print("Your result is is " + str(int(num1)-int(num2)))
  elif int(operation) == 3:
    num1= input("Enter the first number: ")
    num2= input("Enter the second number: ")
    print("Your product is " + str(int(num1)*int(num2)))
  elif int(operation) == 4:
    num1= input("Enter the first number: ")
    num2= input("Enter the second number: ")
    print("Your result is " + str(int(num1)/int(num2)))
  else:
    print("What you have entered is invalid. Please try again.")

  loop = input("Would you like to do more? (yes/no):  ").lower()
  if loop != "yes":
    print("Thank you and have a great day!")
    break

  