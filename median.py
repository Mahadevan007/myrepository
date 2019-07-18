mylist = list(map(int,input().split()))
mylist = sorted(mylist)
if n%2==0:
    print(mylist[int(n/2)])
else:
    print(mylist[int(n-1/2)]+mylist[int(n/2)]/2)
