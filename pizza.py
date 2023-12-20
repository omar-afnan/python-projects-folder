print("Welcome to our pizza shop")

peproni_pizza = 10
sausage_pizza = 15
chicken_pizza = 12

p_p = int(input("How many peproni pizzas would you like sir? "))
s_p = int(input("How many sausage pizzas would you like sir? "))
c_p = int(input("How many chicken pizzas would you like sir? "))

cost_for_p_p = peproni_pizza * p_p
cost_for_s_p = sausage_pizza * s_p
cost_for_c_p = chicken_pizza * c_p

total_cost = cost_for_p_p + cost_for_s_p + cost_for_c_p


amount = float(input("How would you like to pay, sir? "))

if amount >= total_cost:
    change = amount - total_cost
    if change > 0:
        print(f"Thank you for your purchase! Your change is ${change:.2f}")
    else:
        print("Thank you for your exact payment!")
else:
    print("Insufficient funds. Please provide enough money for the purchase.")


print("The total cost for your order is: $", total_cost)
