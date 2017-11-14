
import heapq
import math
import time
import collections

#starts at 1
dictionary_fib = {1:1, 2:2}

def Fib_dp(N):
    if N in dictionary_fib:
        print("found %s in dictionary" % (N,))
        return dictionary_fib[N]
    else:
        print("calculating...")
        dictionary_fib[N] = Fib_dp(N-1) + Fib_dp(N-2)
        print("adding %s to dictionary" % (N,))
        return dictionary_fib[N]

def sum_even_Fibs(max_value):
    idx = 1
    my_sum = 0
    while Fib_dp(idx) < max_value:
        if Fib_dp(idx) % 2 == 0:
            my_sum += Fib_dp(idx)
            print(Fib_dp(idx))
        idx += 1
    
    return my_sum

def find_largest_prime_divisor(N):
    div = 2
    while div < N:
        if (N%div == 0):
            N = N/div
            div -= 1
            print("decrementing  ", div)
        div += 1
    return div

def find_largest_3x3_palindrome():
    a = 999
    b = 999
    my_max_heap = []
    heapq.heapify(my_max_heap)
    
    while b > 99:
        for i in range(a, 99, -1):
            product = i * b
            if str(product) == str(product)[::-1]:
                heapq.heappush(my_max_heap, -product) #O(logN) * N insertions
        b -= 1 #decrement b to 998, 997, etc.... #Constant Time!
    
    return heapq.heappop(my_max_heap)

def find_smallest_evenly_divisible_1_20():
    start = 20
    integers_to_check = range(20, 1, -1)
    still_searching = True
    while still_searching:
        start += 1
        still_searching = False
        for integer in integers_to_check:
            if start % integer != 0:
                still_searching = True
                break

return start


def difference_between_squares(N):
    sum_of_squares = sum([x**2 for x in range(N+1)])
    square_of_sum = sum([x for x in range(N+1)])**2
    return square_of_sum - sum_of_squares


def find_the_nth_prime(N):
    maximum_value = int(math.ceil(N*math.log(N*math.log(N))))
    sieve = list(range(maximum_value))
    sieve_truth_table = [True] * maximum_value #[True for i in range(maximum_value)]
    p = 2
    while (p**2 <= maximum_value):
        if sieve_truth_table[p] is True:
            
            for i in range(p*2, maximum_value, p):
                sieve_truth_table[i] = False

    p += 1

count = 0
    for p in range(2, maximum_value):
        if sieve_truth_table[p]:
            count += 1
            if count == N:
                return p

# start = time.time()
# print find_the_nth_prime(1e6)
# print time.time() - start

# #example of a named tuple!
# BalancedStatusWithHeight = collections.namedtuple('BalancedStatusWithHeight', ('balanced', 'height'))
#
# testing = BalancedStatusWithHeight(True, 0.5)
# print testing.balanced
# print testing.height

test = collections.deque()
test.append(5)
test.appendleft(2)
print(test)

elements = [1, 2, 3]

# for item in elements:
#     print item
#

def get_shifted_element(original_list, shift_to_left, index_in_shifted):
    # back calculate the original index by reversing the left shift
    idx_original = (index_in_shifted + shift_to_left) % len(original_list)
    return original_list[idx_original]

my_list = [1, 2, 3, 4, 5]

print(get_shifted_element(my_list, 1, 2))
#returns 4, since array was shifted left by 1 and 4 now occupies idx 2 in array

print(get_shifted_element(my_list, -2, 3))
#returns 2 because we shift it 2 spots to the right, and we get idx 3


A = [1, 2, 4, 8, 100]
B = [1, 5, 8, 200, 500]



#runtime O(N), memory O(1)
def find_common(A, B):
    common_list = []
    idxA = 0
    idxB = 0
    
    while idxB < len(B) and idxA < len(A):
        if B[idxB] == A[idxA]:
            common_list.append(B[idxB])
            idxB += 1 #increment up
            idxA += 1
        elif B[idxB] < A[idxA]:
            idxB += 1
        elif B[idxB] > A[idxA]:
            idxA += 1

return common_list

print(find_common(A, B)) #should return 1, 8


def find_largest_product_13_integers():
    heap_stack = []
    heapq.heapify(heap_stack) #min-heap
    
    integer_file = open('integers.txt', 'r')
    integers = []
    for line in integer_file:
        line = line.strip()
        if line:
            line = [int(i) for i in line]
            integers.extend(line)

for start_index in range(len(integers)-12):
    integer_slice = integers[start_index:start_index+13]
    integer_product = 1
        for i in integer_slice:
            integer_product*=i
    heapq.heappush(heap_stack, -integer_product)

return -heapq.heappop(heap_stack)

print(find_largest_product_13_integers())

def brute_force_pythagoras():
    for a in range(1, 500):
        for b in range(1, 500):
            c = 1000 - a - b
            if a**2 + b**2 == c**2:
                print(a*b*c)

#return all primes below a value
def return_all_primes_less_than(N):
    maximum_value = N
    sieve = list(range(maximum_value))
    sieve_truth_table = [True] * maximum_value #[True for i in range(maximum_value)]
    p = 2
    while (p**2 <= maximum_value):
        if sieve_truth_table[p] is True:
            
            for i in range(p*2, maximum_value, p):
                sieve_truth_table[i] = False

    p += 1

list_of_primes = []
for p in range(2, maximum_value):
    if sieve_truth_table[p]:
        list_of_primes.append(p)
    
    return list_of_primes
#
# print sum(return_all_primes_less_than(int(2e6)))

def testing_weirdness():
    Bird = collections.namedtuple('Bird', ('name', 'claws'))
    
    return Bird('chicken', 5)

