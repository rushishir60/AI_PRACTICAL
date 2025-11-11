def alpha_beta(depth, index, is_max, values, alpha, beta, max_depth):
    # Stop at leaf node
    if depth == max_depth:
        return values[index]

    if is_max:  # Maximizing player
        best = float('-inf')
        for i in range(2):  # explore left & right child
            val = alpha_beta(depth + 1, index * 2 + i, False, values, alpha, beta, max_depth)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:  # prune branch
                break
        return best

    else:  # Minimizing player
        best = float('inf')
        for i in range(2):
            val = alpha_beta(depth + 1, index * 2 + i, True, values, alpha, beta, max_depth)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:  # prune branch
                break
        return best


# --- MAIN PROGRAM ---
values = [3, 5, 6, 9, 1, 2, 0, -1]  # Leaf node values
max_depth = 3
result = alpha_beta(0, 0, True, values, float('-inf'), float('inf'), max_depth)
print("Optimal value:", result)
