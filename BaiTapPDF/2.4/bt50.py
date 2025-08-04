n=int(input())
t=0
for i in range(1,n+1):
    a=float(input())
    t+=a
t1=t/n
print(f"Diem TB: {t1:.2f}, Xep loai: ",end="")
if t1>=9:print("Xuat sac")
elif t1>=8:print("Gioi")
elif t1>=6.5:print("Kha")
elif t1>=5:print("Trung binh")
else: print("Yeu")