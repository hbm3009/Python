def ucln(a, b):
    while b != 0:
        a, b = b, a % b
    return abs(a)
a=int(input("nhap a: "))
b=int(input("nhap b: "))
print(ucln(a,b))