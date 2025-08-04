a,b,c=map(float,input().split())
if a==0:
    if b==0:
        if c==0:print("Vo so nghiem")
        else:print("Vo nghiem")
    else:print(f"Phuong trinh bac nhat co nghiem: {-c/b}")
else:
    d=b**2-4*a*c
    if d>0:
        x1=(-b + d**0.5)/(2*a)
        x2=(-b - d**0.5)/(2*a)
        print(f"Hai nghiem phan biet: x1 = {x1}, x2 = {x2}")
    elif d==0:print(f"Nghiem kep: x = {-b/(2*a)}")
    else:print("Phuong trinh vo nghiem thuc")
