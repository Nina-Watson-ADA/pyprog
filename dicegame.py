def decide_winner(player1_roll, player2_roll):

    # Check if both numbers are even or both are odd
    if (player1_roll % 2 == player2_roll % 2):
        return "player1"  # player1 wins if both are same (even-even or odd-odd)
    else:
        return "player2"  # player2 wins if one is odd and one is even


# Sample test cases to validate the function
test_cases = [
    (2, 4),  # both even -> player1 wins
    (1, 3),  # both odd -> player1 wins
    (2, 3),  # even/odd -> player2 wins
    (1, 4),  # odd/even -> player2 wins
    (6, 6),  # both even -> player1 wins
    (5, 5),  # both odd -> player1 wins
    (3, 2),  # odd/even -> player2 wins
]

# Loop through the test cases and print results
for p1, p2 in test_cases:
    winner = decide_winner(p1, p2)
    print(f"Player 1 rolled {p1}, Player 2 rolled {p2} => Winner: {winner}")
