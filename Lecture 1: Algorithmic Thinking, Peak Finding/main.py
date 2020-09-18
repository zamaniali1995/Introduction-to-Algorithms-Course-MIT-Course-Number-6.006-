from Algorithms.one_d_first_algorithm import one_d_first_algorithm
from Algorithms.one_d_second_algorithm import one_d_second_algorithm
from Algorithms.two_d_first_algorithm import two_d_first_algorithm
from Algorithms.two_d_second_algorithm import two_d_second_algorithm 

one_d_array = []
for i in range(1000000):
    one_d_array.append(i)

two_d_array = []
tmp = []
for r in range(10000):
    for c in range(10000):
        tmp.append(r*10000+c) 
    two_d_array.append(tmp)
    tmp = []
time_1D_first_alg, peak_1D_first_alg = one_d_first_algorithm(one_d_array)
time_1D_second_alg, peak_1D_second_alg = one_d_second_algorithm(one_d_array)

time_2D_first_alg, peak_2D_first_alg = two_d_first_algorithm(two_d_array)
time_2D_second_alg, peak_2D_second_alg = two_d_second_algorithm(two_d_array)

print('1D array first algorithm:')
print('time:', time_1D_first_alg)
print('peak:', peak_1D_first_alg)

print('1D array second algorithm:')
print('time:', time_1D_second_alg)
print('peak:', peak_1D_second_alg)

print('2D array first algorithm:')
print('time:', time_2D_first_alg)
print('peak:', peak_2D_first_alg)

print('2D array second algorithm:')
print('time:', time_2D_second_alg)
print('peak:', peak_2D_second_alg)
