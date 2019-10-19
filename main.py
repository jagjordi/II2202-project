import genetic

arr = bytearray(3)
arr2 = bytearray(3)
for i in range(0, len(arr2)):
    arr2[i] = 0xff

#genetic.mutate_random_bits(arr, 3)
genetic.swap_random_region(arr, arr2, 4, 4)
genetic.print_bytearray(arr)
genetic.print_bytearray(arr2)
