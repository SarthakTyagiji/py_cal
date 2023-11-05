num_01 = int(input("Enter Number 01 :"))
num_02 = int(input("Enter Number 02 :"))
opr = input("+, -, /, *")
if opr == "+":
    print(num_01+num_02)
elif opr == "-":
    print(num_01-num_02)
elif opr == "*":
    print(num_01*num_02)
elif opr == "/":
    print(num_01/num_02)
else:
    print("Enter Wrong Number and operator")    

