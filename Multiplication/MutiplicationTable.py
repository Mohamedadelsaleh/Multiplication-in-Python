multi = []
while True:
    num = input("Please Enter Your Number: ")
    if num.isnumeric():
        num = int(num)
        break

for num1 in range(1, num + 1):
    multitable = []
    for num2 in range(1, num1 + 1):
        multitable.append(num2 * num1)
    multi.append(multitable)

print("Multiplication Table is: ", multi)
