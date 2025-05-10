# src/knapsack.py

def knapsack(capacity, weights, values, n):
    """
    Solves the 0/1 Knapsack problem.

    Args:
        capacity (float): The maximum amount of capital available.
        weights (list): A list of asset prices.
        values (list): A list of asset expected returns.
        n (int): The number of assets.

    Returns:
        tuple: List of selected assets' indices, maximum return achievable.
    """
    # Initialize the DP table where dp[i][w] represents the maximum value
    # (return) that can be achieved with the first i items and capacity w
    dp = [[0 for _ in range(int(capacity) + 1)] for _ in range(n + 1)]

    # Build the table in a bottom-up manner
    for i in range(1, n + 1):
        for w in range(1, int(capacity) + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - int(weights[i - 1])], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    # Reconstruct the solution (which assets are selected)
    selected_assets = []
    w = int(capacity)
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_assets.append(i - 1)
            w -= int(weights[i - 1])

    return selected_assets, dp[n][int(capacity)]
