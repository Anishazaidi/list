a=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
i=0
while i<len(a):
    j=0
    while j<len(a):
        if a[i]>a[j]:
            j=j+1
        i=i+1
    print(a[i])   


