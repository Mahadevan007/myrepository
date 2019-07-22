points=[]
for i in range(4):
	p1,q1=input().split()
	points.append(int(p1))
	points.append(int(q1))
if len(set(points))>2:
	print("no")
else:
	print("yes")
