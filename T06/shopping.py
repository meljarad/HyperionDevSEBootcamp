# SHOPPING.PY T06 TASK 2

# Asks the user to input the names of three different products
product1_name = input("Enter the name of your first product:\n")
product2_name = input("Enter the name of your second product:\n")
product3_name = input("Enter the name of your third product:\n")

# Asks the user for the price of each product
product1_price = round(float(input("Enter the price of your first product:\n")),2) # Round() is employed to automatically round the input to 2 decimal places
product2_price = round(float(input("Enter the price of your second product:\n")),2)
product3_price = round(float(input("Enter the price of your third product:\n")),2)

# Calculate and print the total of all three products and average price
price_total = product1_price + product2_price + product3_price
avg_price = round(price_total/3,2)
print(f"The Total of {product1_name}, {product2_name}, {product3_name} is R{price_total:.2f} and the average price is R{avg_price:.2f}.") #.2f used to always print prices to 2 decimal places
