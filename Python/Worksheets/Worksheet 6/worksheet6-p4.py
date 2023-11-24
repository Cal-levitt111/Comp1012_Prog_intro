my_dict = {'a': 500, 'b': 200, 'c': 1500, 'd': 20, 'x': 1550, 'v': 260}
max = list(my_dict.values())[0]
min = list(my_dict.values())[0]
for key, value in my_dict.items():
    if value > max:
        max = value
    
    if value < min:
        min = value

print(max, min)
