num = int(input())
mylist = list(map(int,input().split()))
mydict = {}
anslist = []
for i in mylist:
    if i in mydict:
        mydict[i] += 1
        if mydict[i]>=2:
            anslist.append(mydict[i])
        else:
            pass
    else:
        mydict[i] = 1
if len(anslist)==0:
    print('uniquwe')
else:
    print(anslist[0])
        
