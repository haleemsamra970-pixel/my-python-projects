num1 = int(input("inter the first number: "))
choise = input("chose[+,-,/,*]: ")
num2 = int(input("iner the second number: "))

if choise == "+":
  total = num1 + num2
  print(f"{total} = {num1} + {num2}")
elif choise == "-":
  total = num1 - num2
  print(f"{total} = {num1} - {num2}")
elif choise == "/":
  total = num1 / num2
  print(f"{total} = {num1} / {num2}")
elif choise == "*":
  total = num1 * num2
  print(f"{total} = {num1} * {num2}")
 