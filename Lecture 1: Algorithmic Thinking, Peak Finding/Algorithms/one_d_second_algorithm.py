import time
def one_d_second_algorithm(array): 
    s = time.time()
    peak_value = peak(0, len(array), array)
    e = time.time()
    return peak_value, e-s

def peak(start, stop, array):
        mid = (start+stop)//2
        if(mid > 0 and array[mid] < array[mid-1]):
            return peak(start, mid, array)
        elif(mid < len(array)-1 and array[mid] < array[mid+1]):
            return peak(mid, stop, array)
        else:
            return array[mid]