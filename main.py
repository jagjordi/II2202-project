import genetic as gen
import verification as ver

arr = bytearray(3)
arr2 = bytearray(3)
for i in range(0, len(arr2)):
    arr2[i] = 0xff

gen.mutate_random_bits(arr, 3)
gen.swap_random_region(arr, arr2, 4, 4)
ver.print_bytearray(arr)
ver.print_bytearray(arr2)

g = ver.encode_grey(4)
print(g)
n = ver.decode_grey(g)
print(n)

gen_str_list = [bytearray(3), bytearray(3), bytearray(3)]
for i in range(0, 500):
    gen_str_list = gen.next_generation(gen_str_list,
                                       3, 2, 3, 2,
                                       lambda gs: gs[0] + gs[1] + gs[2])
    print(gen_str_list)
                                
