string = input()
characters = ",./<>?:;'{[}]|\_-+=~`!@#$%^&*()}'"
count = 0
for i in string:
    if i in characters:
        count = count+1
print(count)
