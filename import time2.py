import time

# Function for Cycle Sort in descending order
def cycle_sort(arr):
    n = len(arr)
    for cycle_start in range(n - 1):
        item = arr[cycle_start]
        pos = cycle_start
        for i in range(cycle_start + 1, n):
            if arr[i] > item:  # For descending order
                pos += 1

        if pos == cycle_start:
            continue

        while item == arr[pos]:
            pos += 1
        arr[pos], item = item, arr[pos]

        while pos != cycle_start:
            pos = cycle_start
            for i in range(cycle_start + 1, n):
                if arr[i] > item:
                    pos += 1
            while item == arr[pos]:
                pos += 1
            arr[pos], item = item, arr[pos]

# Function to run the game
def dragon_tiger_game():
    # Get the number of players
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

    # Sort bet amounts with Cycle Sort and measure time in nanoseconds
    start_time = time.time_ns()
    cycle_sort(bet_amounts)
    end_time = time.time_ns()

    # Arrange sorted players based on sorted bet amounts
    sorted_players = sorted(players, key=lambda x: x[1], reverse=True)
    print("\nSorted Players by Bet Amount:")
    for player, bet in sorted_players:
        print(f"Player {player} - Bet Amount: {bet}")

    # Display runtime in nanoseconds with decimal precision
    runtime = end_time - start_time
    print(f"\nCycle Sort Runtime: {runtime:.2f} nanoseconds")

# Run the game
dragon_tiger_game()
