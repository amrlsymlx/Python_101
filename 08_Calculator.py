num1 = float(input("Input Num1:"))
op = input("Enter operator:")
num2 = float(input("Input Num2:"))

add_result = num1+num2
sub_result = num1-num2
mul_result = num1*num2
div_result = num1/num2

if op == "+":
    print(num1+num2)
elif op == "-":
    print(num1-num2)
elif op == "/":
    print(num1/num2)
elif op == "*":
    print(num1*num2)
else:
    print("Invalid Operator!")