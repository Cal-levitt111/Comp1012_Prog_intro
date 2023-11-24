dict1 = {'sc0011': 'Ali Bin Ahmad', 'sc0012': 'Wong Fei Hung', 'sc0013': 'James Purple', 'sc0014': 'Salimah Wahid'}
dict2 = {'it1011': 'Abdus Salam', 'it1012': 'Alex Chung', 'it1013': 'Anastasia Zeus', 'it1014': 'Vihaan Arjun'}
dict3 = {'ai2011': 'Charles Lewin', 'ai2012': 'Apollo Leto', 'ai2013': 'Ciarra Vega', 'ai2014': 'Lara Gould'}
dict4 = {}

for item in (dict1, dict2, dict3):
    dict4.update(item)

print(dict4)