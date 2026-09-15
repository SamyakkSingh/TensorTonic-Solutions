import numpy as np

def manhattan_distance(x: list, y: list) -> float:
    # Convert input lists to NumPy arrays as required
    x_arr = np.array(x)
    y_arr = np.array(y)
    
    # Compute Manhattan distance using vectorized absolute differences and sum
    return float(np.sum(np.abs(x_arr - y_arr)))