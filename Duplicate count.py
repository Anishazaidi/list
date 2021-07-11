list=[1,2,2,3,4,4,5,5,6]
i=0
b=[]
while i<len(list):
    if list[i] not in b:
        b.append (list[i])
        i=i+1
j=0
