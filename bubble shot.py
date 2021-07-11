# num=[50,40,70,56,12,5,10,7]
# m=0
# i=0
# s_max=0
# while i<len(num):
#     if num[i]>m:
#         m=num[i]
#         s_max=m
#     elif num[i]<s_max and num[i]>m:
#         s_max=m[i]
#     i=i+1
# print(s_max)







a=[5,-5,6,-4]
i=0
while i<len(a):
    j=0
    while j<(len(a)-1):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
        j=j+1
    i=i+1                              
print(a)
print(a[1])

