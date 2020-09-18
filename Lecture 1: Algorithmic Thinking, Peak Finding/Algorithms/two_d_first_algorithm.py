import time
def two_d_first_algorithm(array):
    s = time.time()
    peak_value = peak(array)
    e = time.time()
    return peak_value, e-s

def peak(array):
    row_size = len(array)
    col_size = len(array[0])
    for r in range(row_size):
        for c in range(col_size):
            if (r==0 and c==0 and array[r][c]>array[r+1][c] and array[r][c]>array[r][c+1]):
                return array[r][c]
            elif (r==0 and c==col_size-1 and array[r][c]>array[r+1][c] and array[r][c]>array[r][c-1]):
                return array[r][c]
            elif (r==row_size-1 and c==0 and array[r][c]>array[r-1][c] and array[r][c]>array[r][c+1]):
                return array[r][c]
            elif (r==row_size-1 and c==col_size-1 and array[r][c]>array[r-1][c] and array[r][c]> array[r][c-1]):
                return array[r][c]
            elif(r==0 and c!=0 and c!=col_size-1 and array[r][c]>array[r][c-1] and array[r][c]>array[r][c+1] and array[r][c]>array[r+1][c]):
                return array[r][c]
            elif(c==0 and r!=0 and r!=row_size-1 and array[r][c]>array[r][c+1] and array[r][c]>array[r-1][c] and array[r][c]>array[r+1][c]):
                return array[r][c]
            elif(r==row_size-1 and c!=0 and c!=col_size-1 and array[r][c]>array[r][c+1] and array[r][c]>array[r][c-1] and array[r][c]>array[r-1][c]):
                return array[r][c]
            elif(c==col_size-1 and r!=0 and r!=row_size-1 and array[r][c]>array[r][c-1] and array[r][c]>array[r-1][c] and array[r][c]>array[r+1][c]):
                return array[r][c]
            elif(r!=0 and c!=0 and r!=row_size-1 and c!=col_size-1 and array[r][c]>array[r][c-1] and array[r][c]>array[r][c+1] and array[r][c]>array[r+1][c] and array[r][c]>array[r-1][c]):
                return array[r][c]