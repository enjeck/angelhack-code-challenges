# Question 4: Find the group’s efficiency

def groupEfficiency(group):
    # When we sort, we bring the elements with minumum differences next to each other
    group.sort()
    min_cost = float("inf")
    for i in range(len(group)):
        # For each work, we exclude them and calculate the cost without that worker
        group_without_worker = group[:i] + group[i+1:]
        cost = 0
        for j in range(0, len(group_without_worker), 2):
            cost += group_without_worker[j+1] - group_without_worker[j]
        # Get the minumum for each excluded worker
        min_cost = min(cost, min_cost)
    
    return min_cost

workers = [1, 3, 54, 712, 52, 904, 113, 12, 135, 32, 31, 56, 23, 79, 611, 123, 677, 232, 997, 101, 111,
123, 2, 7, 24, 57, 99, 45, 666, 42, 104, 129, 554, 335, 876, 35, 15, 93, 13]

# 475
print(groupEfficiency(workers))

# ANALYSIS
# Time complexity: O(n**2), where n is the length of the input list. This comes from the fact that we have a two nested loops that go through the input list
# Space complexity: O(1)