#second largest
n=int(input())
lt=[]
for i  in range(n):
   lt.extend(map(int,input().split()))
   print(lt)
max=lt[0]
secondmax=float('-inf')
for num in lt:
    if num>max:
        secondmax=max
        max=num
    elif num>secondmax and num!=max:
        secondmax=num    
print(secondmax) 
