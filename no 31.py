a=int(input("enter a"))
b=1
sum=0
for i in range(1,a+1):
    b=i*b
    sum=sum+b
    print(sum,end=",")