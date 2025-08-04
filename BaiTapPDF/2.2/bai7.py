def sodao(n):
    am = n < 0
    n = abs(n)
    ket_qua = 0
    while n > 0:
        chu_so = n % 10
        ket_qua = ket_qua * 10 + chu_so
        n //= 10
    return -ket_qua if am else ket_qua
n=int(input("Nhap n: "))
print(sodao(n))