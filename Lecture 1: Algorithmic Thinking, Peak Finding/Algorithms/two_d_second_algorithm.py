import time
def two_d_second_algorithm(array): 
    s = time.time()
    peak_value = peak(0, len(array), array)
    e = time.time()
    return e-s, peak_value

def peak(start_row, stop_row, array):
    mid_row = (start_row+stop_row)//2
    mid_array = array[mid_row]
    idx_max = mid_array.index(max(mid_array))
    if ( mid_row>0 and array[mid_row][idx_max]<array[mid_row-1][idx_max]):
        return peak(start_row, mid_row, array)
    elif (mid_row<len(array)-1 and array[mid_row][idx_max]<array[mid_row+1][idx_max]):
        return peak(mid_row, stop_row, array)
    else:
        return array[mid_row][idx_max]