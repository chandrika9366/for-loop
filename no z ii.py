a=int(input("enter a"))
for i in range(1,a+1):
    for j in range(1,6-i):
        print(" ",end="")
    for k in range(i,0,-1):
        print(k,end="") 
    for k in range(k+1,i+1):
        print(k,end="")   
    print()         