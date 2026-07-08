import math

def elu(x, alpha):
    """
    Apply ELU activation to each element.
    """
    result=[]
    for item in x:
        if item > 0:
            result.append(float(item))
        else:
            activated_value=alpha*(math.exp(item)-1)
            result.append(activated_value)
    return result        
    # Write code here