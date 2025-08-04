a,b,c,d,e,f=map(float,input().split())
D=a*e-b*d
Dx=c*e-b*f
Dy=a*f-c*d
if D!=0:
    x=Dx/D
    y=Dy/D
    print(f"x = {x}, y = {y}")
elif Dx==0 and Dy==0:print("Vo so nghiem")
else:print("Vo nghiem")
