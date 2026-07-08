import numpy as np
import math
vectorized_erf=np.vectorize(math.erf)


def gelu(x):
    """
    Compute the Gaussian Error Linear Unit (exact version using erf).
    x: list or np.ndarray
    Return: np.ndarray of same shape (dtype=float)
    """
    x=np.asarray(x)
    result=1/2*x*(1+vectorized_erf(x/np.sqrt(2)))
    return result
    # Write code here
    pass
