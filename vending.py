#Items that are to be displayed
items={ 'B001':{'item_name':'Orange Juice',
        'item_price':4,
        'quantity':5},
        'B002':{'item_name':'Mango Juice',
        'item_price':4,
        'quantity':6},
        'B003':{'item_name':'Iced Coffee',
        'item_price':5,
        'quantity':4},
        'B004':{'item_name':'Carbonated Water',
        'item_price':3,
        'quantity':2},
        'S001':{'item_name':'Salted Chips',
        'item_price':3,
        'quantity':6},
        'S002':{'item_name':'Vanilla Wafers',
        'item_price':3,
        'quantity':5},
        'S003':{'item_name':'Caramel Popcorn',
        'item_price':6,
        'quantity':4},
        'S004':{'item_name':'Chocolate Wafers',
        'item_price':5,
        'quantity':7},
        'C001':{'item_name':'Mini Snickers',
        'item_price':3.5,
        'quantity':2},
        'C002':{'item_name':'Reeses Cups',
        'item_price':3.5,
        'quantity':6},
        'C003':{'item_name':'Mini Pretzels',
        'item_price':4.5,
        'quantity':3},
        'C004':{'item_name':'Dark Chocolate',
        'item_price':5,
        'quantity':5},
}

#Suggestions that are included in the Vending Machine
suggestions={
    'Iced Coffee':'Chocolate Wafers',
    'Dark Chocolate':'Carbonated Water',
    'Mango Juice':'Salted Chips',
    'Mini Pretzels':'Iced Coffee',
    'Reeses Cups':'Orange Juice',
    'Caramel Popcorn':'Mini Snickers'
}

#To display the menu of the Vending Machine
def display_item():
 print("Welcome to the the Vending Machine. Available items are:")
 for code, item in items.items():
  print(f"Code:{code}\tItem:{item['item_name']}\tPrice:AED{item['item_price']}\tQuantity:{item['quantity']}")

#Function of the Vending Machine
def vending_machine():
 code=input('ENTER CODE OF AN ITEM:')
 if code in items:
  item=items[code]['item_name']
  price=items[code]['item_price']
  quantity=items[code]['quantity']
  print(f"Selected item:{item}\nPrice: AED {price}\nQuantity:{quantity}")

  amount=float(input("Please insert coins: AED " ))
  if amount < price:
   print('Insufficient amount')
  else:
   change=amount - price
   print(f"Dispensing {item}...\nPlease collect your change of AED {change:.2f}" )
   items[code]['quantity']-=1
   print(f"Items left for {item}:{items[code]['quantity']}")

# Adding suggestions to the Vending Machine
   if item in suggestions:
    suggestion=suggestions[item]
    print(f"If you bought {item},you might also like {suggestion}.")
   else:
    print("Thankyou for buying")
 else:
  print("Invalid selection")

#Running the display item function
display_item()

#Running the Vending machine function
vending_machine()

