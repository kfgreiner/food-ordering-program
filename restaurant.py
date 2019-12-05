print('Welcome to "Basic Restaurant"')

partyQuantity=int(input('How many people are in your party?'))

menu = dict(item1="Cheese Sticks ($2.00)", item2="Sandwich ($5.00)",
            item3="Salad ($8.00)", item4="Burger ($10.00)",
            item5="Cake ($5.00)")
orderBalance=0

for i in range(1,int(partyQuantity)+1,1):
    print("Type 1 to order a menu item, or 0 to skip an item")
    option1=int(input(menu["item1"]))
    if option1==1:
            orderBalance=2.0+orderBalance
    else:
            orderBalance=0.0+orderBalance
    option2=int(input(menu["item2"]))
    if option2==1:
            orderBalance=5.0+orderBalance
    else:
            orderBalance=0.0+orderBalance
    option3=int(input(menu["item3"]))
    if option3==1:
            orderBalance=8.0+orderBalance
    else:
            orderBalance=0.0+orderBalance
    option4=int(input(menu["item4"]))
    if option4==1:
            orderBalance=10.0+orderBalance
    else:
            orderBalance=0.0+orderBalance
    option5=int(input(menu["item5"]))
    if option5==1:
            orderBalance=5.0+orderBalance
    else:
            orderBalance = 0.0 + orderBalance
    print("Total cost of food items: $", orderBalance)
tax=(0.0825*orderBalance)
total=(orderBalance+tax)
print("Total cost of tax (8.25%): $", round(tax,2))
print("Total cost with taxes: $",round(total,2))
