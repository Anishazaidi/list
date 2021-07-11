a=[1,5,3]
# print(a[-1:-5])


i=0
while i<len(a):
    i=i+1
    if a[i] or a[-1]:
        break  
print(a[i])