# Question 4: Find the group’s efficiency

def groupEfficiency(group):
    group.sort()
    min_cost = float("inf")
    for i, worker in enumerate(group):
        group_without_worker = group[:i] + group[i+1:]
        cost = 0
        for j in range(0, len(group_without_worker), 2):
            cost += group_without_worker[j+1] - group_without_worker[j]
        
        min_cost = min(cost, min_cost)
    
    return min_cost

w = [1, 3, 54, 712, 52, 904, 113, 12, 135, 32, 31, 56, 23, 79, 611, 123, 677, 232, 997, 101, 111,
123, 2, 7, 24, 57, 99, 45, 666, 42, 104, 129, 554, 335, 876, 35, 15, 93, 13]

# 475
print(groupEfficiency(w))