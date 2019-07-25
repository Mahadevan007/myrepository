n = int(input())
digit = []
while(n>0):
    rev = n%10
    digit.append(rev)
    n//=10
print(*reversed(digit))
