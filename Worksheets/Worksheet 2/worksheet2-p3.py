sentence = input()
vowels = ["a", "e", "i", "o", "u"]
count = 0
for i in range(0, len(sentence)-1):
    if sentence[i].lower() in vowels:
        count += 1

print (count)
