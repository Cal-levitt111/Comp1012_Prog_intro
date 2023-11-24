answers = []
my_nums = ((5, 10, 15, 20),  (2, 4, 6, 8), (57, 68, 79, 81), (1, 3, 5, 7))
for n in range(len(my_nums)):
    answers.append(0)

print(answers)
for i in my_nums:
    temp_list = list(i)
    for x in range(len(temp_list)):
        answers[x] += temp_list[x]
        print(answers)

print(answers)
