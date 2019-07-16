num = int(input())
count = 0
for i in range(0,num):
	if i%num==0:
		count = count + 1
if count==2:
	print("yes")
else:
	print("no")
