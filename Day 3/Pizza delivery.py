# Create a basic pizza delivery program

print("Welcome to the Python Pizza Deliveries App!")

# Variables
bill = 0


# Ask for size of pizza
size = input("Do you want a 's', 'm' or 'l' Pizza?\n").lower()
# Work out bill based on size
while size != "s" and size != "m" and size != "l":
  size = input("Do you want a 's', 'm' or 'l' Pizza?\n").lower()

if size == "s":
  bill += 100
elif size == "m":
  bill += 120
elif size == "l":
  bill += 140


# Ask if they want pepperoni 
pepperoni = input ("Do you want pepperoni? 'y' or 'n'.\n")
# Work out bill with Pepperoni
if pepperoni == "y":
  if size == "s":
    bill += 25
  else:
    bill += 30  

# Ask if they want extra cheese
extra_cheese = input("Do you want extra cheese? 'y' or 'n'.\n")
# Work out final amount with cheesse
if extra_cheese == "y":
  bill += 20

print(f"Your final bill is: N${bill:.2f}")

