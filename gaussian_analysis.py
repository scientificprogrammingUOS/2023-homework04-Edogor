import numpy as np

# implement the function gaussian_analysis

def gaussian_analysis(loc, scale, lower_bound, upper_bound):
    if type(loc)!=int  or type(scale)!=int or type(lower_bound)!=int or type(upper_bound)!=int:
        raise TypeError("alle werte sollen integer sein")
    y = np.random.normal(loc, scale, size=100)
    newY = y[(y>=lower_bound) & (y<=upper_bound)]
    m = np.mean(newY)
    s = np.std(newY)

    return (m, s)

if __name__ == "__main__":
    gaussian_analysis(2, 2, 0, 100)