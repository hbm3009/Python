a,b=map(int,input().split())
def nam(n):
    if n%4==0 and (n%100!=0 or n%400==0):return True
    else: return False
if a in [1,3,5,7,8,10,12]:print(31)
elif a in[4,6,9,11]:print(30)
else:
    if nam(b):print(29)
    else: print(28)