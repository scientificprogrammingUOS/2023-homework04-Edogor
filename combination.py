import numpy as np 

# implement your function to combine two numpy arrays 

def combination(arr1, arr2, ax=0):
    arr1 = np.squeeze(arr1)
    arr2 = np.squeeze(arr2)
    
    if np.can_cast(arr1.dtype, arr2.dtype) == False:
        raise ValueError("the arrays cannt be casted")

    return np.concatenate((arr1, arr2), axis=ax)

if __name__ == "__main__":
    combination([1, 2, 3],  [4, 5, 6])