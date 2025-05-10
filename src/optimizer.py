# src/optimizer.py
import argparse
import matplotlib.pyplot as plt
from src.utils import load_assets
from src.knapsack import knapsack

def plot_frontier(risk_list, return_list, filename="frontier.png"):
    """
    Plots the risk-return frontier.

    Args:
        risk_list (list): List of portfolio risks.
        return_list (list): List of portfolio returns.
        filename (str): The file to save the plot as.
    """
    plt.scatter(risk_list, return_list, color='green')
    plt.xlabel("Risk (Standard Deviation)")
    plt.ylabel("Expected Return")
    plt.title("Efficient Frontier")
    plt.grid(True)
    plt.savefig(filename)
    plt.close()

def main():
    # Parsing command line arguments
    parser = argparse.ArgumentParser(description="Portfolio Optimizer")
    parser.add_argument('--capital', type=float, required=True, help="Total capital available for investment")
    parser.add_argument('--risk', type=float, required=True, help="Maximum acceptable risk level (0-100)")
    parser.add_argument('--csv', type=str, required=True, help="Path to the assets CSV file")
    parser.add_argument('--plot', action='store_true', help="Generate risk-return plot")
    args = parser.parse_args()

    # Load assets from CSV
    assets_df = load_assets(args.csv)

    # Prepare lists for asset prices, returns, and risks
    prices = assets_df['Price'].tolist()
    returns = assets_df['ExpectedReturn(%)'].tolist()
    risks = assets_df['RiskScore'].tolist()

    # Perform knapsack optimization based on user input (capital, risk tolerance)
    selected_assets, expected_return = knapsack(args.capital, prices, returns, len(assets_df))

    # Print the selected assets and the expected return
    print(f"Selected assets: {', '.join(assets_df.iloc[selected_assets]['Ticker'])}")
    print(f"Expected Return: {expected_return:.2f}%")

    # Plot the efficient frontier if requested
    if args.plot:
        plot_frontier(risks, returns)

if __name__ == "__main__":
    main()
