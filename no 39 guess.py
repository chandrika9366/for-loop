a=int(input("enter a"))
for i in range(1,a+1):
    b=int(input("enter b"))
    if b==a:
        print("you guess right")
        break
    else:
        print("not divisible")