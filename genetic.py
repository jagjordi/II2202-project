import struct
import random

#
# UTILITY
#

def print_bytearray(arr):
    for b in arr:
        print(hex(b), ' ', end='')
    print('')

def get_bit(arr, n):
    byte_n = n // 8
    bit_n = 7 - n % 8
    byte = arr[byte_n]
    if byte & (1 << bit_n):
        return 1
    else:
        return 0

def set_bit(arr, n, val):
    byte_n = n // 8
    bit_n = 7 - n % 8
    byte = arr[byte_n]
    if (val > 0):
        byte |= (1 << bit_n)
    else:
        byte &= ~(1 << bit_n)
    arr[byte_n] = byte

#
# MUTATION
#
    
# Alter nth bit in the bytearray.
def mutate_one_bit(arr, n):
    bit = get_bit(arr, n)
    if bit > 0:
        set_bit(arr, n, 0)
    else:
        set_bit(arr, n, 1)

# Alter random number of, [0, max_n], random bits in the array
def mutate_random_bits(arr, max_n):
    assert max_n >= 0
    n = random.randint(0, max_n)
    for i in range(n):
        bit_n = random.randint(0, len(arr) * 8 - 1)
        mutate_one_bit(arr, bit_n)

#
# CROSSOVER
#

def swap_region(arr1, arr2, start, length):
    print(start, length)
    for i in range(start, start + length):
        temp = get_bit(arr1, i)
        set_bit(arr1, i, get_bit(arr2, i))
        set_bit(arr2, i, temp)

def swap_random_region(arr1, arr2, max_len, max_n):
    assert len(arr1) == len(arr2)
    assert max_len >= 1
    assert max_len <= len(arr1) * 8
    assert max_n >= 0

    n = random.randint(0, max_n)    
    for i in range(0, n):
        length = random.randint(1, max_len)
        offset = random.randint(0, len(arr1) * 8 - length)
        swap_region(arr1, arr2, offset, length)

#
# SELECTION
#

# TODO



