n=int(input())
s=""
while n!=0:
    t=n%2
    s=str(t)+s
    n//=2
if s=="":print(0)
print(s)