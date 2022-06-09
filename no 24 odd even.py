a=int(input("enter a"))
sum_even=0
sum_odd=0
for i in range(1,a+1):
    if i%2==0:
        sum_even=sum_even+i
    else:
        sum_odd=sum_odd+i    
print("sum_even",sum_even) 
print("sum_odd",sum_odd)       