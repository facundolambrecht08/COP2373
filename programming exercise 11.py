from deck import Deck   # This imports the Deck class from Section 11.5
                        # Make sure deck.py (from the book) is in the same folder.

def deal_hand(deck, num_cards=5):
    """Deals num_cards from the deck and returns them as a list."""
    hand = []
    for _ in range(num_cards):
        hand.append(deck.pop_card())
    return hand

def replace_cards(hand, deck, positions):
    """
    Replace cards in 'hand' at the given positions (list of ints).
    Positions use 1–based indexing (1 = first card).
    """
    for pos in positions:
        index = pos - 1
        if 0 <= index < len(hand):
            hand[index] = deck.pop_card()
    return hand

def print_hand(hand, title="Hand"):
    """Displays cards in the hand."""
    print(f"\n{title}:")
    for i, card in enumerate(hand, start=1):
        print(f"{i}: {card}")

def main():
    # Create and shuffle deck
    deck = Deck()
    deck.shuffle()

    # Deal initial 5–card hand
    hand = deal_hand(deck)
    print_hand(hand, "Your initial hand")

    # Prompt user for cards to replace
    user_input = input("\nEnter card numbers to replace (e.g. 1 3 5) or press Enter to keep all: ")

    if user_input.strip():
        try:
            positions = [int(x) for x in user_input.split()]
        except ValueError:
            print("Invalid input. No cards replaced.")
            positions = []
    else:
        positions = []

    # Replace selected cards
    final_hand = replace_cards(hand, deck, positions)
    print_hand(final_hand, "Your final hand after draw")

if __name__ == "__main__":
    main()
