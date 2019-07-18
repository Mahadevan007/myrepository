noofele = int(input())
mylist = list(map(int,input().split()))
mylist = sorted(mylist)
for i in mylist:
  print(i,end=" ")
