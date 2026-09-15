import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    N = len(A)
    M = len(A[0])

    result = np.zeros((M,N),dtype = float)

    for i in range(N):
        for j in range(M):
            result[j][i] = A[i][j];
    return result