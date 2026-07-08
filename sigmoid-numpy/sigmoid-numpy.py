import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    # Write code here
    x_values=np.array(x)
    result=1/(1+np.exp(-x_values))
    return result
    pass