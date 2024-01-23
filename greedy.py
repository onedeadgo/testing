def greedy_coin_change(coins, target_amount):
    coins.sort(reverse=True)  # Sort coins in descending order
    
    change = []  # List to store the selected coins
    
    for coin in coins:
        while target_amount >= coin:
            # Take as many coins of the current denomination as possible
            change.append(coin)
            target_amount -= coin

    return change

# Example usage:
coins = [25, 10, 5, 1]
target_amount = 63

result = greedy_coin_change(coins, target_amount)
print(f"Greedy solution for {target_amount} cents: {result}")

