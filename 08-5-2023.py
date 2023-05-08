# Question 3: Is the permutation divisible by 7?

def genPermutations(n):
    n = list(str(n))
    permutations = []
    def dfs(p, remaining_elements):
        if not remaining_elements:
            permutations.append(p)
            return
        for i, n in enumerate(remaining_elements):
            dfs([n]+p, remaining_elements[:i]+remaining_elements[i+1:])
    dfs([], n)
    for i, p in enumerate(permutations):
        permutations[i] = int(''.join(p))
    return permutations

def divisibleBy7(permutation_array):
    divisible_permutations = []
    for p in permutation_array:
        if p % 7 == 0:
            divisible_permutations.append(p)
    divisible_permutations.sort()
    if divisible_permutations:
        return (divisible_permutations[0] + divisible_permutations[-1]) / 2
    else:
        return 0

arr = genPermutations(1867)
# 5152.0
print(divisibleBy7(arr))
