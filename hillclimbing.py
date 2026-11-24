def hill_climbing(f, x, step=0.01, max_iter=1000):
    for _ in range(max_iter):
        # Look at left and right neighbors, pick the best one
        best_next = max([x - step, x + step], key=f)
        
        if f(best_next) > f(x):
            x = best_next      # Climb up
        else:
            break              # Reached peak (local maxima)
            
    return x, f(x)

# --- Main ---
expr = input("Enter function of x (e.g., -x**2 + 4*x): ")
f = lambda x: eval(expr)
start = float(input("Enter starting value: "))

x_max, y_max = hill_climbing(f, start)
print(f"Maxima at x = {x_max:.4f}, value = {y_max:.4f}")