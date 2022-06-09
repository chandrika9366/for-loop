a=int(input("enter a"))
for i in range(1,a//2):
    if a%i==0:
        print("not prime")
        break
else:
    print("prime")    