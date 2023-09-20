Number = int(input("Enter the Number"))
value = int(input("Enter the value"))
for i in range(Number):
    product = i * value
    if i == 2:
        continue
    print(str(i) +  " x " + str(value) + " = " + str(product))