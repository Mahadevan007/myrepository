string1 = input()
mydict = {}
for i in string1:
    if i in mydict:
        mydict[i] += 1
    else:
        mydict[i] = 1
mylist = []
for i in mydict:
    if mydict[i] == 1:
        mylist.append(i)
print(len(mylist))
