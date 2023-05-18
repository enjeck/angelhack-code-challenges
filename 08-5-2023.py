# Question 3: Is the permutation divisible by 7?

# Helper function to get all the permutations of any number
def genPermutations(n):
    # Converting number to list of digits to allow looping over its digits
    n = list(str(n))
    permutations = []
    # Permutations are gotten recursively
    def permute(p, remaining_elements):
        if not remaining_elements:
            permutations.append(p)
            return
        for i, n in enumerate(remaining_elements):
            permute([n]+p, remaining_elements[:i]+remaining_elements[i+1:])
    permute([], n)
    # Convert the lists of digits back to integers to permit numeric operations later
    for i, p in enumerate(permutations):
        permutations[i] = int(''.join(p))
    return permutations

def divisibleBy7(permutation_array):
    divisible_permutations = [] # This list contains all the permuations divisible by 7
    for p in permutation_array:
        if p % 7 == 0:
            divisible_permutations.append(p)
    
    # When we sort, we know the smallest and largest values are at the front and back of the list respectively
    divisible_permutations.sort()
    if divisible_permutations:
        return (divisible_permutations[0] + divisible_permutations[-1]) / 2
    return 0

arr = genPermutations(1867)
# 5152.0
print(divisibleBy7(arr))
