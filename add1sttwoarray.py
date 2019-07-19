num = int(input())
mylist = list(map(int,input().split()))
for i in range(num):
    for j in range(num):
        for k in range(num):
            if(mylist[i]+mylist[j]==mylist[k]) and i<j<k:
                print('{} {} {}'.format(mylist[i],mylist[j],mylist[k]))
