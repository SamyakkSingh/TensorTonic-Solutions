import numpy as np

def euclidean_distance(x: list, y: list) -> float:
    """
    Returns the Euclidean distance as a Python float.
    """
    x_arr = np.array(x)
    y_arr = np.array(y)

    distance = np.sqrt(np.sum((x_arr-y_arr)**2))

    return float(distance)
    