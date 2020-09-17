print('Please enter 1D array:')
one_d_array = int(input())

print('Please enter the 2D array:')
two_d_array = int(input())

time_1D_first_alg, peek_1D_first_alg = one_d_first_algorithm()
time_1D_second_alg, peek_1D_second_alg = one_d_second_algorithm()

time_2D_first_alg, peek_2D_first_alg = two_d_first_algorithm()
time_2D_second_alg, peek_2D_second_alg = two_d_second_algorithm()

print('1D array first algorithm:\n')
print('time:', time_1D_first_alg)
print('peek:', peek_1D_first_alg)

print('1D array second algorithm:\n')
print('time:', time_1D_second_alg)
print('peek:', peek_1D_second_alg)

print('2D array first algorithm:\n')
print('time:', time_2D_first_alg)
print('peek:', peek_2D_first_alg)

print('2D array second algorithm:\n')
print('time:', time_2D_second_alg)
print('peek:', peek_2D_second_alg)

