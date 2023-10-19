n_List = [[],
          [],
          [],
          [],
          []]

for i in range(0, 5):
    for j in range(0, 5):
        n_List[i].append((i * 5) + j)

print("[", end="")

for i in range(4):
    print(n_List[i], "," , sep="")


print(n_List[4], "]", sep="")