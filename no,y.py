k=1
for i in range(1,5):
    for l in range(1,5-i):
        print(" ",end=" ")
    for j in range(1,k+1):
        print("*",end=" ")
    k=k+2
    print()        