# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

from art import logo
print(logo)
bids = {}
are_there_new_bidder = True
while are_there_new_bidder:
    name = input("What is your name?")
    bid = float(input("What is your bid?"))
    bids[name] = bid
    is_there_anyone_else = input("Do you have anyone else? that would like to bid? (yes/no)").lower()
    if is_there_anyone_else != "yes":
        are_there_new_bidder = False
    else:
        print("\n" * 100)

max_bid = 0
max_bidder = None
for name, bid in bids.items():
    if bid > max_bid:
        max_bidder = name
        max_bid = bid

print(f"Max bidder: {max_bidder} with bid {max_bid}")







