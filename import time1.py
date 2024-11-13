import time
import random

# Function for Bingo Sort
def bingo_sort(arr):
    highest = max(arr)
    next_highest = highest
    while True:
        current_highest = -float('inf')
        for value in arr:
            if value < next_highest:
                current_highest = max(current_highest, value)
        if current_highest == -float('inf'):
            break
        for i in range(len(arr)):
            if arr[i] == next_highest:
                arr[i] = current_highest
        next_highest = current_highest
    return arr

# Function to run the game
def dragon_tiger_game():
    # Get number of players
    num_players = int(input("Enter the number of players (max 100): "))
    if num_players > 100 or num_players < 1:
        print("Please enter a valid number of players between 1 and 100.")
        return

    # Get bet amounts for each player
    players = []
    for i in range(num_players):
        bet_amount = float(input(f"Enter the bet amount for player {i + 1}: "))
        players.append((i + 1, bet_amount))  # Store player number and bet amount

    # Extract only the bet amounts for sorting
    bet_amounts = [bet for _, bet in players]

    # Sort bet amounts with Bingo Sort and measure time in nanoseconds
    start_time = time.time_ns()
    bingo_sort(bet_amounts)
    end_time = time.time_ns()

    # Display sorted players by their bet amounts
    sorted_players = sorted(players, key=lambda x: x[1], reverse=True)
    print("\nSorted Players by Bet Amount:")
    for player, bet in sorted_players:
        print(f"Player {player} - Bet Amount: {bet}")

    # Display runtime in nanoseconds
    runtime = end_time - start_time
    print(f"\nBingo Sort Runtime: {runtime:2f} nanoseconds")

# Run the game
dragon_tiger_game()
