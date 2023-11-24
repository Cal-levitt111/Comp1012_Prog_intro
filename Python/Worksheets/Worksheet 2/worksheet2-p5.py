name = list(input())
for i in range(0,len(name)):
    if name[i].isalpha():
        if name[i].isupper():
            name[i] = "X"
        else:
            name[i] = "x"

print("".join(name))