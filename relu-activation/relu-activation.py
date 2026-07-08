import numpy as np

def relu(x):
    """
    Implement ReLU activation function.
    """
    inputs=np.array(x)
    return np.maximum(0,x)
    
    output=relu(inputs)
    print(output)
    # Write code here
    pass