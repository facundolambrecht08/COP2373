Python 3.13.6 (v3.13.6:4e665351082, Aug  6 2025, 11:22:35) [Clang 16.0.0 (clang-1600.0.26.6)] on darwin
Enter "help" below or click "Help" above for more information.
>>> # Cinema Ticket Pre-Sale Program
... # Each buyer can buy up to 4 tickets
... # Only 20 tickets available total
... 
... def buy_tickets(available):
...     """Ask the buyer how many tickets they want and return the number bought"""
...     tickets = int(input("How many tickets would you like (max 4)? "))
...     if tickets > 4:
...         print("Sorry, you can only buy 4 tickets max.")
...         tickets = 4
...     if tickets > available:
...         print("Only", available, "tickets left, you will get that many.")
...         tickets = available
...     return tickets
... 
... def show_remaining(available):
...     """Show how many tickets are still available"""
...     print("Tickets left:", available)
... 
... def main():
...     total_tickets = 10
...     buyers = 0
... 
...     while total_tickets > 0:  # loop until all tickets sold
...         print("\n--- New Buyer ---")
...         bought = buy_tickets(total_tickets)   # function call
...         total_tickets -= bought               # accumulator
...         buyers += 1                           # count buyers
...         show_remaining(total_tickets)         # function call
... 
...     print("\nAll tickets are sold out!")
...     print("Total buyers:", buyers)
... 
... # Run the program
