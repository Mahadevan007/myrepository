string = input()
lengt = len(string)
mylist = []
for i in range(0,lengt,2):
    mylist.append(string[i:i+2][::-1])
print("".join(mylist))
