list = [6,1,3,5,6,3,1]
i=0
m=1
b=[]
while i<len(list):
    if list[i] not in  b:
        b.append(list[i])
        print(b)
        m=m*b[i]
    i=i+1
print(m)
    
    
