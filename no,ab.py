k=1
for i in range(1,6):
    for j in range(1,6-i):
        print(" ",end="")
    for l in range(1,k+1):
        print(i,end="")
    k=k+2
    print()        