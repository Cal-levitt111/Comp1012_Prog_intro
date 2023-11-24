dict_num = {'even': [], 'odd': []}
for i in range(1,51):
    if i % 2 == 0:
        dict_num["even"].append(i)
    else:
        dict_num["odd"].append(i)
print(dict_num)