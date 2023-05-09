import numpy as np

# implement the function strange pattern

def strange_pattern(shape):
    n = shape[0]
    m = shape[1]
    a = np.zeros((n,m), dtype=bool)
    
    for i in range(n):
        f = 0-i
        while(f < m):
            if (f>=0) and (f<=m):
                a[i][f] = True
            f += 3

    return a

if __name__ == "__main__":
    print(strange_pattern((10, 10)))