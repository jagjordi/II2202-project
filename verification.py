# Verification code

import genetic as gen

#
# UTILITY
#

def print_bytearray(arr):
    for b in arr:
        print(hex(b), ' ', end='')
    print('')

def encode_grey(n):
    return n ^ (n >> 1)

def decode_grey(n):
    mask = n >> 1
    while mask != 0:
        n = n ^ mask
        mask = mask >> 1
    return n

# def byte_len(lst):
#     tot_len = 0
#     for item in lst:
#         tot_len += ctypes.sizeof(item)
#     return tot_len


# (4).to_bytes(2, 'big')
# arr[1:2] = (4).to_bytes(2, 'big')
