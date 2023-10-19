num_str = [[],[]]
userstring = input()
for item in list(userstring):
    if item.isnumeric():
        num_str[0].append(item)
    elif item.isalpha():
        num_str[1].append(item)

print(num_str)