# Question 2: Who’s the fastest runner?

import heapq

def whoIsTheFastestRunner(time):
    
    # Using a heap to keep track of the changes of each runner
    heap = [[0, 0, 'John', False], # [time to update, distance travelled so far, name (used as key for data dictionary),  resting or not (True if resting)]
                    [ 0, 0, 'James',False],
                    [ 0, 0, 'Jenna', False],
                    [ 0, 0, 'Josh',False],
                    [ 0, 0, 'Jacob',False],
                    [ 0, 0, 'Jerry', False]
                    ]
    heapq.heapify(heap)

    k = 0
    res = 0
    while k <= time and heap:
        # At each point in time, we check if we can update the distance or running/resting status of each runner
        while heap and heap[0][0] == k:
            update_time, distance, name, is_resting = heapq.heappop(heap)
            speed, running_time, rest_time = constants[name]
            # If the runner had been resting, make them resume running by updating the distance and status
            if is_resting:
                if update_time + rest_time > time:
                    res = max(distance, res)
                    continue
                update_time += rest_time
                is_resting = False
            else:
                if update_time + running_time > time:
                    res = max(distance, res)
                    continue
                
                distance += (speed * running_time)
                update_time += running_time
                is_resting = True

            heapq.heappush(heap, [update_time, distance, name, is_resting])
        k += 1
    return res

constants = {
    'John': [10, 6, 20], # [Speed, Running Time, Rest Time]
    'James': [8, 8, 25],
    'Jenna': [12, 5, 16],
    'Josh': [7, 7, 23],
    'Jacob': [9, 4, 32],
    'Jerry': [5, 9, 18]
}

# 3540
print(whoIsTheFastestRunner(1234))