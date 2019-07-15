num = input()
temp = num
summ = 0
while(num > 0):
    rem = num % 10
    summ = summ + rem
    num = num/10
return temp == summ
