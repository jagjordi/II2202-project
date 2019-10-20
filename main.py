import verification as ver
import genetic as gen

# One solution is a list of couples.
# A couple is a parameter and its byte size.
# E.g. [[30 , 4], [45.4, 4]]

solutions = [[[30 , 4], [45.4, 4]], 
             [[21 , 4], [94.1, 4]],
             [[123, 4], [34.67, 4]]]

def print_sols(sols):
    for sol in sols:
        print(sol)

print('Initial solutions: ')
print_sols(solutions)

# A function to score each solution.  For this example, we want the
# sum of parameters to be as close as possible to zero.
def sol_score(sol):
    return -abs(sol[0] + sol[1])

def apply_genetic_custom(sols, gen_n):
    return ver.apply_genetic(sols,
                             4,     # max_mutation_bit_n
                             4,     # max_crossover_len
                             3,     # max_crossover_n_per_gs
                             gen_n, # n_generation
                             sol_score)

solutions = apply_genetic_custom(solutions, 15)
print('Optimized solutions after 15 generations: ')
print_sols(solutions)

solutions = apply_genetic_custom(solutions, 85)
print('Optimized solutions after 100 generations: ')
print_sols(solutions)

solutions = apply_genetic_custom(solutions, 400)
print('Optimized solutions after 500 generations: ')
print_sols(solutions)
