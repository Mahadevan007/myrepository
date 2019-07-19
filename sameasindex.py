num = int(input())
mylist = list(map(int,input().split()))
anslist = []
for i in range(0,num):
    if i==mylist[i]:
        anslist.append(i)
if(len(anslist)>1):
    print(*anslist)
else:
    print(-1)
