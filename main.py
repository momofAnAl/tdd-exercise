VALID_CARDS = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']

def blackjack_score(hand):

    if len(hand) > 5:
        return "Invalid"
    
    score = 0
    ace_count = 0
    
    for card in hand:
        if card not in VALID_CARDS:
            return "Invalid"
        
        if isinstance(card, int):
            score += card
        elif card.isalpha() and card != "Ace":
            card = 10 
            score += card
        elif card == "Ace":  
            if score > 10:
                card = 1
            else:
                card = 11
            score += card
            ace_count += 1
                    
    while score > 21 and ace_count > 0:
        score -= 10
        ace_count -= 1
        
    if score > 21:
        return "Bust"   
    
    return score
