num = int(input())
a=0
b=1
if num <= 1:
    return num
print(1)
for i in range(0,num-1):
                     c = a+b
                     a = b
                     b = c
                     print(c)
