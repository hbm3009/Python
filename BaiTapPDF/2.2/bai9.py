def shh(n):
    if n <= 1:
        return False
    tong_uoc = 0
    for i in range(1, n):
        if n % i == 0:
            tong_uoc += i
    return tong_uoc == n
n=int(input("nhap n: "))
print(shh(n))