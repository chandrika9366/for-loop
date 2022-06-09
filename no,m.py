a=int(input("enter a"))
k=1
for i in range(1,a+1,2):
    for j in range(1,i+1):
        print(k,end="")
        k=k+1
    print()