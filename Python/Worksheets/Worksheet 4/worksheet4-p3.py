final_list = []

input_list = [1, 2, 1, 3, 'a', 'b', "a", 'c']

for item in input_list:

    found = False

    for sublist in final_list:

        if item in sublist:
            sublist.append(item)
            found = True

    if found == False:
        final_list.append([item])

print(final_list)