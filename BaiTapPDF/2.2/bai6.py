def tcs(n):
    n = abs(n)
    tong = 0
    while n > 0:
        chu_so = n % 10
        tong += chu_so 
        n = n // 10
    return tong
n=int(input("Nhap n: "))
print(tcs(n))