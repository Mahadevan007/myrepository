n = int(input())
mylist = list(map(int,input().split()))
mydict = {}
for i in mylist:
    if i in mydict:
        mydict[i] += 1
    else:
        mydict[i] = 1
anslist = []
for i in mydict:
    if mydict[i]>1:
        anslist.append(i)
anslist = sorted(anslist)
print(*anslist)
