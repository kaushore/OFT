The UI is made in streaamlit.
The backend is using fastApi.

To run this package, please add openAI_key in the line 17 and 37 of api.py

In the command line, please execute the scripts:

python api.py

streamlit run app.py --server.port 9801


p.s. For testing purpose, I'm using GPT-3.5 turbo as as I don't have subscription of GPT-4. 


def shortest_robot_distance(A):
    from collections import defaultdict
    
    N = len(A)
    
    # Group shelves by item numbers
    shelves = defaultdict(list)
    for i in range(N):
        shelves[A[i]].append(i)
    
    # Sort items and shelves for each item
    items = sorted(shelves.keys())
    
    # Initialize DP table
    dp = [[float('inf')] * 2 for _ in range(len(items))]
    
    # Base case for the first item
    first_item_shelves = shelves[items[0]]
    dp[0][0] = abs(0 - first_item_shelves[0])  # Distance from start to the first shelf of the first item
    dp[0][1] = abs(0 - first_item_shelves[-1])  # Distance from start to the last shelf of the first item
    
    # Fill DP table
    for i in range(1, len(items)):
        current_shelves = shelves[items[i]]
        previous_shelves = shelves[items[i - 1]]
        
        # Minimum distance to the first shelf of the current item
        dp[i][0] = min(dp[i - 1][0] + abs(previous_shelves[0] - current_shelves[0]),
                       dp[i - 1][1] + abs(previous_shelves[-1] - current_shelves[0]))
        
        # Minimum distance to the last shelf of the current item
        dp[i][1] = min(dp[i - 1][0] + abs(previous_shelves[0] - current_shelves[-1]),
                       dp[i - 1][1] + abs(previous_shelves[-1] - current_shelves[-1]))
    
    # Return to the start
    last_item_shelves = shelves[items[-1]]
    min_distance = min(dp[-1][0] + abs(last_item_shelves[0] - 0),
                       dp[-1][1] + abs(last_item_shelves[-1] - 0))
    
    return min_distance

# Example usage:
A = [1, 3, 3, 2, 2, 1]
print(shortest_robot_distance(A))  # Output should be the shortest distance
