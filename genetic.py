# Genetic algorithm framework

import random
import copy

#
# UTILITY
#

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
# INTERFACE
#

def next_generation(gen_str_list, max_mutation_bit_n,
                    max_crossover_couple_n, max_crossover_len,
                    max_crossover_n_per_gs, gs_score_fn):
    offsprings = copy.deepcopy(gen_str_list)
    
    # Apply mutation
    for gs in offsprings:
        mutate_random_bits(gs, max_mutation_bit_n)

    # Apply crossover
    crossover_couple_n = random.randint(0, max_crossover_couple_n)
    for i in range(0, crossover_couple_n):
        gs_idx_1 = 0
        gs_idx_2 = 0
        while gs_idx_1 == gs_idx_2:
            gs_idx_1 = random.randint(0, len(offsprings) - 1)
            gs_idx_2 = random.randint(0, len(offsprings) - 1)
        swap_random_region(offsprings[gs_idx_1],
                           offsprings[gs_idx_2],
                           max_crossover_len, max_crossover_n_per_gs)

    # Apply selection
    gen_str_list += offsprings
    scores = map(gs_score_fn, gen_str_list)
    list_with_scores = map(
        lambda gs, s: [gs, s],
        gen_str_list, scores)
    list_with_scores = list(list_with_scores)
    list_with_scores.sort(key=lambda i: i[1], reverse=True)
    list_with_scores = list_with_scores[0:len(list_with_scores)//2]
    new_gen_str_list = map(lambda i:i[0], list_with_scores)
    
    # Return final list
    return list(new_gen_str_list)


