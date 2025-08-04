import random
n=random.randint(1,100)
while True:
    x=int(input())
    if x>n:print("Lon hon")
    elif x<n:print("Nho hon")
    else:
        print("Dung roi")
        break