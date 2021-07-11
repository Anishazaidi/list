# a="3"
# b="4"
# c=int(3)
# d=int(4)
# e=(c+d)
# g=str(e)
# print(g)
# print(type(g))
num=[50,40,70,56,12,5,10,7]
# find out max and sec max in list
max=0
i=0
secondmax=0
while i<len(num):
    if num[i]>max:
        secondmax=max
        max=r[i]
    elif secondmax<r[i] and max>num[i]:
        secondmax=num[i]
    i=i+1
print(secondmax)        
