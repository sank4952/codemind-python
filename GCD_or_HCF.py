a,b=map(int,input().split())
if a>b:
    min=b
else:
    min=a
for i in range(1,min+1):
    if a%i==0 and b%i==0:
        hcf=i
print(hcf)    
    
    