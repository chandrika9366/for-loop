a=int(input("enter a"))
b=1
sum=0
print(b,end="")
for i in range(2,a+1):
    if i%2==0:
        b=i**2
        print("+",b,end="")
    else:
        print("-",i**2,end="")    