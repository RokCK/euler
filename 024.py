# Problem 024: Lexicographic Permutations

import itertools

digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
permutations = list(itertools.permutations(digits))

millionth_permutation = permutations[999999]
print(''.join(map(str, millionth_permutation)))
