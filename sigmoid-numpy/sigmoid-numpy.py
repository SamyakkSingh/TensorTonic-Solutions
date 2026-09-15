import numpy as np

def sigmoid(x: list | float) -> np.ndarray | float:
    is_scalar = np.isscalar(x)
    
    arr = np.asarray(x, dtype=float)
    
    # Numerically stable piecewise sigmoid
    result = np.where(
        arr >= 0,
        1.0 / (1.0 + np.exp(-arr)),
        np.exp(arr) / (1.0 + np.exp(arr))
    )
    
    if is_scalar:
        return float(result)
    
    return result