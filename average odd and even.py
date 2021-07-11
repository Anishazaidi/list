marks= [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
even_c=0
even_s=0
even_a=0
odd_s=0
odd_c=0

while i<len(marks):
    if marks[i]%2==0:            
       even_s=even_s+(marks[i])
    even_c=even_c+1
    average_even=even_s/even_c
    i=i+1
else:
    odd_s=odd_s+1
    odd_c=odd_c+1
    average_odd=odd_s/odd_c
print(odd_s,"odd sum")
print(even_s,"even sum")
print(odd_c,"odd count")
print(even_c,"even count")
print(average_even,"average count")
print(average_odd,"average")











       
