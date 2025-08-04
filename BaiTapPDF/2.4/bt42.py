n=float(input())
if n<=1:t=n*15000
elif n<=5:t=15000+(n-1)*12000
else: t=15000+4*12000+(n-5)*10000
print(int(t))