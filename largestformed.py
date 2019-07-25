n = int(input())
num = list(map(int,input()))
rem = []
while n!=0:
    maxi = max(num)
    rem.append(maxi)
    i = num.index(maxi)
    del num[i]
    n = n-1
ans = "".join(str(i) for i in rem)
print(int(ans))
