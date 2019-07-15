n,k = map(int,input().split())
mylist = list(map(int,input().split()))
sum = 0
for nums in mylist[0:k]:
    sum = sum + nums
print(sum)
