n,q = map(int,input().split())
oddlist = []
for i in range(n+1,q):
	if i%2==0:
		print(i,end=" ")
