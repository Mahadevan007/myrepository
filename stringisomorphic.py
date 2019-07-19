string1,string2 = input().split()
if len(string1) != len(string2):
    print("No")
else:
    for i in range(0,len(string1)):
        if string1.count(string1[i])==string2.count(string2[i]):
            print("yes")
            break
        else:
            print("no")
            break
