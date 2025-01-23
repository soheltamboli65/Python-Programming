a = int(input("Enter the Number: "))
b = int(input("Enter the Number: "))
c = int(input("Enter the Number: "))

if a > b and a > c:
    print(a, "is the greatest number")
elif b > a and b > c:
    print(b, "is the greatest number")
else:
    print(c, "is the greatest number")
