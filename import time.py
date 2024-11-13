import time

# Iterative Quick Sort function
def iterative_quick_sort(arr):
    # Stack for storing subarrays that need to be sorted
    stack = [(0, len(arr) - 1)]
    
    # Iteration counter
    iterations = 0
    
    # Continue while there are subarrays in the stack
    while stack:
        start, end = stack.pop()
        if start < end:
            pivot_index = partition(arr, start, end)
            # Push the left and right subarrays onto the stack
            stack.append((start, pivot_index - 1))
            stack.append((pivot_index + 1, end))
        iterations += 1
    
    return arr, iterations

# Partition function for quick sort
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Main program
def dragon_tiger_game():
    # Get number of players
    num_players = int(input("Enter the number of players: "))
    
    # Get bets from each player
    bets = []
    for i in range(num_players):
        bet = int(input(f"Enter the bet amount for player {i+1}: "))
        bets.append(bet)
    
    # Start timer
    start_time = time.time_ns()
    
    # Sort bets using iterative quick sort
    sorted_bets, iterations = iterative_quick_sort(bets)
    
    # End timer
    end_time = time.time_ns()
    execution_time = end_time - start_time
    
    # Display sorted bets
    print("\nBets sorted from lowest to highest:")
    for i, bet in enumerate(sorted_bets, start=1):
        print(f"Player {i} bet: {bet}")
    
    # Calculate winners and losers
    half = num_players // 2
    winners = sorted_bets[half:]
    losers = sorted_bets[:half]
    
    print("\nGame Outcome:")
    print(f"Number of players who won: {len(winners)}")
    print(f"Number of players who lost: {len(losers)}")
    
    # Show execution time and iterations in nanoseconds
    print(f"\nExecution time: {execution_time} nanoseconds")
    print(f"Number of iterations in sorting: {iterations}")

# Run the game
dragon_tiger_game()