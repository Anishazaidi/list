magic_square=[[8,3,4],[1,5,9],[6,7,2]]
i=0
r_sum=0
c_sum=0
while i <len(magic_square):
	j=0
	while j<len(magic_square):
		r_sum=r_sum+magic_square[i][j]
		c_sum=c_sum+magic_square[j][i]
		j=j+1
		i=i+1
c=0
d=0
f=0
d_1=0
d_2=0
while c<len(magic_square):
		d_1=d_1+magic_square[c][d]
		d_2=d_2+magic_square[c][f]
		c=c+1
		d=d+1
		f=f-1
if r_sum and c_sum ==d_1 and d_2:
		print("magic_sqare")
else:
		print("not")