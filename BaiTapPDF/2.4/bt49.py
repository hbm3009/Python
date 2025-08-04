a,b=map(float,input().split())
c=input()
if c=="+":t=a+b
elif c=="-":t=a-b
elif c=="*":t=a*b
elif c=="/":
    t=a/b
    if b==0:t="Loi"
print(t)
