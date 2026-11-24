board = [' '] * 9
WINS = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]

def win(p):
    return any(board[a] == board[b] == board[c] == p for a, b, c in WINS)

def show():
    for i in range(0, 9, 3):
        print(" | ".join(board[i:i+3]))
    print("-" * 9)

def dfs(is_ai):
    if win('X'): return 1
    if win('O'): return -1
    if ' ' not in board: return 0

    best = float('-inf') if is_ai else float('inf')
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X' if is_ai else 'O'
            score = dfs(not is_ai)
            board[i] = ' '
            best = max(best, score) if is_ai else min(best, score)
    return best

# --- Game Loop ---
while True:
    show()
    move = int(input("Enter position (0-8): "))
    board[move] = 'O'
    if win('O') or ' ' not in board: break

    # AI finds best move
    best_move = max((i for i in range(9) if board[i] == ' '),
                    key=lambda i: (board.__setitem__(i, 'X'), s := dfs(False), board.__setitem__(i, ' '), s)[3])
    board[best_move] = 'X'
    if win('X') or ' ' not in board: break

show()
print("AI wins!" if win('X') else "You win!" if win('O') else "Draw!")