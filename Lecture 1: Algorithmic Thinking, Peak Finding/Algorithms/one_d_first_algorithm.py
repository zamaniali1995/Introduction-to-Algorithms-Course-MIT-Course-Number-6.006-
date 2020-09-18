
import time
def one_d_first_algorithm(array): 
    s = time.time()
    peak_value = peak(array)
    e = time.time()
    return peak_value, e-s

def peak(array):
    array_size = len(array)
    for i in range(array_size):
        if (i==0 and array[0]>array[1]):
            return array[0]
        elif (i==array_size-1 and array[array_size-1]>array[array_size-2]):
            return array[array_size-1]
        elif (array[i]>array[i+1] and array[i]>array[i-1]):
            return array[i]