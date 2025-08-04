def ucln(a,b):
    if b==0: return a
    return ucln(b,a%b)
a,b=map(int,input().split())
print(f"UCLN {ucln(a,b)}, BCNN: {(a*b)//ucln(a,b)}")