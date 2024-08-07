# Bill Cost
amount = float(input("How much is the bill?\n"))

# Amount Tip %
tip_percentage = int(input("How much % tip would you like to give?\n"))

# Amount People
amount_people = int(input("How many people will split the bill?\n"))

# Work out everything

# Tip
tip = (tip_percentage / 100) * amount

# Total amount
total_amount = amount + tip

# Total split through all People
split_total = total_amount / amount_people

print(f"If you split the bill between {amount_people} people, each person would pay: {split_total:.2f}")