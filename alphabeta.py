def alphabeta(leaves, depth, alpha, beta, is_max):
    # Base case: reached leaf node
    if depth == 0 or len(leaves) == 1:
        return leaves[0]

    mid = len(leaves) // 2
    children = [leaves[:mid], leaves[mid:]]  # Split into left and right subtrees

    if is_max:
        val = float('-inf')
        for child in children:
            val = max(val, alphabeta(child, depth - 1, alpha, beta, False))
            alpha = max(alpha, val)
            if beta <= alpha:
                break  # Beta cut-off
        return val
    else:
        val = float('inf')
        for child in children:
            val = min(val, alphabeta(child, depth - 1, alpha, beta, True))
            beta = min(beta, val)
            if beta <= alpha:
                break  # Alpha cut-off
        return val

# --- Main ---
leaves = list(map(int, input("Enter leaf values: ").split()))
depth = int(input("Enter tree depth: "))

print("Optimal Value:", alphabeta(leaves, depth, float('-inf'), float('inf'), True))