# 배낭 문제(Knapsack Problem)

def knapsack(weights, values, capacity):
	n = len(weights)

	dp = [[0] * (capacity + 1) for _ in range(n+1)]

	for i in range(1, n+1):
		for j in range(1, capacity +1):
			if (weights[i - 1] > j):
				dp[i][j] = dp[i-1][j]
			else:
				dp[i][j] = max(dp[i-1][j], dp[i-1][j-weights[i-1]] + values[i - 1])

	return dp[n][capacity]

weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 7

print(knapsack(weights, values, capacity))