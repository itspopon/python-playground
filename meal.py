meal = ["eggs", "bacon", "beans", "sausages"]
# meal = ["eggs", "bacon", "spam", "sausages"]

nastyFoodItem = ''

for item in meal:
    if item == "spam":
        nastyFoodItem = item
        break
else:
    print("I'll have a plate of that")

if nastyFoodItem == "spam":
    print("Ew! DISGUSTING")