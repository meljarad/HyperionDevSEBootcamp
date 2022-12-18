#T22 TASK 1 - CAFE.PY

# Initial variable declaration for four items in the cafe
cafe_items = ['americano', 'cappuccino', 'latte', 'espresso']
total_stock_value = 0

# Dictionary used to store the stock levels (i.e. there are 20 americanos available)
stock_dict = {'americano': 20,
              'cappuccino': 25,
              'latte': 30,
              'espresso': 40
              }

# Dictionary used to store the prices for each items
item_prices = {'americano': 1.99,
              'cappuccino': 2.99,
              'latte': 2.50,
              'espresso': 1.50
              }

# Prints border, title and description to the user for readability and UI purposes
border_length = 65
print('─'*border_length, "\nSTOCK WORTH CALCULATOR")
print("\nThis program will calculate the total worth of stock for each item:\n")

# Loops through each item and retrieves corresponding value by using the list element as a key in .get() reference
for i in range(0,len(cafe_items)):
    print(f"ITEM {i+1}: {cafe_items[i].upper()}")
    print("\tStock amount:", "\t"*9, f"{stock_dict.get(cafe_items[i])} AVAILABLE")
    print(f"\tItem price:", "\t"*9, f"£{item_prices.get(cafe_items[i]):.2f}")
    print(f"\tValue of stock:", "\t"*8, f"£{item_prices.get(cafe_items[i])*stock_dict.get(cafe_items[i]):.2f}")
    total_stock_value += item_prices.get(cafe_items[i])*stock_dict.get(cafe_items[i]) # Cumulative total of total stock worth

# Final output of total stock value to the user
print('─'*border_length) # Prints border for readability and UI purposes
print(f"TOTAL STOCK VALUE:", "\t"*9, f"£{total_stock_value:.2f}")
print('='*border_length)
