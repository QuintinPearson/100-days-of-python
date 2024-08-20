
# Find the highest bidder
def find_highest_bidder(bidders):
    '''
    function
    '''
    current_bid = 0
    current_highest_bidder = ""
    for key in bidders:
        if bidders[key] > current_bid:
            current_bid = bidders[key]
            current_highest_bidder = f"{key} has the Highest bid of {bidders[key]}"

    return current_highest_bidder

# Create a dictionary
bidders = {}

while True:
    # User name is the key
    current_bidder = input("Who is bidding?\n")

    # User bid is the value
    current_bidder_value = int(input("What is your bid?\n"))

    bidders[current_bidder] = current_bidder_value

    # Ask for any other bidders
    add_bidder = input("Are there any other bidders? 'y' or 'n'\n").lower()
    if add_bidder == 'n':
        break

# Loop through the dictionary and find the highest bidder
highest_bidder = find_highest_bidder(bidders)

print(highest_bidder)
