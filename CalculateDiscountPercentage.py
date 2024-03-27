cart_amount = float(input("Enter the cart amount: "))

if cart_amount < 100:
    discount_percentage = 5
elif cart_amount <= 200:
    discount_percentage = 10
else:
    discount_percentage = 15

discount = cart_amount * discount_percentage / 100
total_cost = cart_amount - discount

print("Discounted amount: $", discount)
print("Total cost: $", total_cost)