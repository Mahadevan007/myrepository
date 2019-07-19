num = int(input())
mylist = list(map(int,input().split()))
anslist = []
for i in range(0,num):
    if i%2==0:
        if mylist[i]%2!=0:
            anslist.append(mylist[i])
        else:
            pass
    else:
        if mylist[i]%2==0:
            anslist.append(mylist[i])
        else:
            pass
print(*anslist)
    
