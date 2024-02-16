list = []
for x in range(10):
    num = int(input("enter a number: "))
    list.append(num)
max = 0
for x in list:
    if x > max:
        max = x
print(f"the biggest number is: {max}")