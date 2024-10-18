from statistics import quantiles

food_items={
"Idly" :25,
"MASALA dOSA" :65,
"Coffee" :15,
"Tea" :15,
"Rice Items":35

        }#Dictionary of food items and their price tag.
bill_amount=0
items={}
is_processing=True
while is_processing :

    print("#########MENU")
    for food_items,price in food_items.items():
        print(f"{food_items} : ₹{price:.2f}")
        item = int(input("Enter the food item from the list above: or(Q) to Quit : ").title()
         if item.lower()=="q":

        quantity=int(input("Enter the quantity of food U want:"))
        items[item]=food_items[item]*quantity






















while is_processing :
    print("############################Menu#################################")
    for food_item,price in food_items.items():
        print(f"{food_item.upper()}:₹ {price:.2f}")
        item=input("Enter the food item from the list above :or (Q to quit):").title()
        if item.