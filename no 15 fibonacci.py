a=int(input("enter a"))
b=0
c=1
d=0
print(b,c,end=",")
for i in range(1,a+1):
    d=b+c
    b=c
    c=d
    print(d,end=",")