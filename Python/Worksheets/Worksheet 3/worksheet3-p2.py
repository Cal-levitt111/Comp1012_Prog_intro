print("This program will evaluate whether you are elligible to buy alcohol")
age = int(input("enter age"))
legal_age = int(input("enter legal age"))
paid_by_card = input("card? Y or N")
age_on_id = int(input("Id age"))
estimated_age = int(input("estimate age"))
sell = False

if (age == age_on_id and age >= legal_age) or paid_by_card.lower() == "y" or estimated_age > 21:
    sell = True

print (sell)