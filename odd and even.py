 
elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43] 
i=0
c=0
d=0
while i<len(elements):
    if elements[i]%2==0:
        c=c+1    
    else:
        d=d+1
    i=i+1
print(c,"even")
print(d,"odd")

  
