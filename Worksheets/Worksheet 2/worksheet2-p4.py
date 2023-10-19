sentence = input()
vowels = ["a", "e", "i", "o", "u"]
seen = []
count = 0
for i in range(0, len(sentence)-1):
    a = sentence[i].lower()
    if  a in vowels and a not in seen:
        seen.append(a)
        count += 1

print (count)
