d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
d3 = {}

for i, j in d1.items():
    for p, q in d2.items():
        if i == p:
            sum1 = j + q
            d3.update({p:sum1}) 

print(d3)