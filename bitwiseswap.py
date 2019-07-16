a,b = map(int,input().split())
a = a xor b
b = a xor b
a = a xor b
print(a,b)
