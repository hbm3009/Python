def snt(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
n = int(input("nhap n: "))
if snt(n):
    print("la snt")
else:
    print("ko la snt")