# Verification code

import genetic as gen
import struct
import copy

#
# UTILITY
#

def print_bytearray(arr):
    for b in arr:
        print(hex(b), ' ', end='')
    print('')

# TODO make grey work with bytes
def encode_grey(n):
    return n ^ (n >> 1)

def decode_grey(n):
    mask = n >> 1
    while mask != 0:
        n = n ^ mask
        mask = mask >> 1
    return n

# Float only bocomes 4 bytes.
def get_grey_bytes(item, n):
    data = 0;
    if isinstance(item, int):
        data = item.to_bytes(n, 'big')
    elif isinstance(item, float) and n == 4:
        data = struct.pack('>f', item)
    else:
        raise TypeError('get_bytes not supported for ' +
                        str(type(item)) + ' with size ' + n + '.')
    #data = encode_grey(data)
    return data

# ref is [num, byte_len]
def from_grey_bytes(bts, ref_n):
    #bts = decode_grey(bts)
    data = 0
    if isinstance(ref_n, int):
        data = int.from_bytes(bts, 'big')
    elif isinstance(ref_n, float) and len(bts) == 4:
        data = struct.unpack('>f', bts)[0]
    else:
        raise TypeError('from_bytes not supported for ' +
                        str(type(ref_n)) + 'with size ' + len(bts) + '.')
    return data

# Create genetic string from e.g. [[2, 4], [2.3, 4]]
# Input: list of couples of item and byte length.
def list_with_size_to_gs(lst):
    arr = bytearray(0)
    for item in lst:
        arr += bytearray(get_grey_bytes(item[0], item[1]))
    return arr 

# size is list of byte lengths
def gs_to_list_with_size(arr_grey, ref_list):
    arr = copy.copy(arr_grey)
    lst = copy.deepcopy(ref_list)
    idx = 0
    for i in range(len(lst)):
        ref_n = lst[i][0]
        size = lst[i][1]
        n = from_grey_bytes(arr[idx:idx+size], ref_n)
        lst[i] = [n, size]
        idx += size
    return lst
        
    

# def byte_len(lst):
#     tot_len = 0
#     for item in lst:
#         tot_len += ctypes.sizeof(item)
#     return tot_len


# (4).to_bytes(2, 'big')
# arr[1:2] = (4).to_bytes(2, 'big')
