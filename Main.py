# Ask the user to input the cost price and selling price
cost_price = float(input("Enter the cost price: "))
selling_price = float(input("Enter the selling price: "))

# Calculate the profit or loss
profit = selling_price - cost_price

# Check if there is profit or loss
if profit > 0:
  # Calculate the profit percentage
  profit_percentage = (profit / cost_price) * 100
  print(f"The profit percentage is {profit_percentage}%")
elif profit < 0:
  # Calculate the loss percentage
  loss_percentage = (profit / cost_price) * 100
  print(f"The loss percentage is {loss_percentage}%")
else:
  print("There is no profit or loss.")
