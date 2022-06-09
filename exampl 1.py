a=int(input("enter a"))
for i in range(1,a+1):
    for j in range(1,i+1):
        if i==j or j==1 or i==a:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()             