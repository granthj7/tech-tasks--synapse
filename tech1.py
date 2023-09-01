c=int(input("Input the starting number of the range "))
d=int(input("Input the last number of the range "))
divisors=[]
result={}
for i in range(c,d):
    z=0
    for j in range(i):
        if i%(j+1)==0:
            z=z+1
            divisors.append(j+1)
    if z>2:
        result[i]=divisors
    else:
     result[i]=bin(i)[2:] 
     divisors=[]
print(result)