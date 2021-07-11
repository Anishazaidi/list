
elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43] 
i=0
s=0
d=0
while i<len(elements):
    if elements[i]%2==0:
        s=s+elements[i]
    else:
        d=d+elements[i]
    i=i+1
print(s,"even")
print(d,"odd")