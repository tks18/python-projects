from replit import clear
#HINT: You can call clear() to clear the output in the console.

from art import logo
print(logo);

bids = {}

biddingFinished = False

def find_highest_bidder(bidding_record):
  bidding_amount = 0
  bidding_name = '';
  for record in bidding_record:
    if(bidding_record[record] > bidding_amount):
      bidding_amount = bidding_record[record]
      bidding_name = record
  print(f"The Winner is {bidding_name} and the Prize is {str(bidding_amount)}")


while not biddingFinished:
  name = input("What is Your Name ? ")
  price = int(input("What is Your Bid? $"))
  bids[name] = price
  should_continue = input("Are there any Other Bidders? y/n").lower()
  if should_continue == 'n':
    biddingFinished = True;
    find_highest_bidder(bids)
  elif should_continue == 'y':
    clear();
