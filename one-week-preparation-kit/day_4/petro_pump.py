petrolpumps = [[1,5],[3,4], [10,3], [2,4]]


def truckTour(net_pumps):
    net_pumps = [pump[0]-pump[1] for pump in petrolpumps]
    # net_pumps = [3,-1,-1,-1,-1,2,2,-1,2]
    for i in range(len(net_pumps)):
        # print(i)
        actual_pumps = net_pumps[i:] + net_pumps[:i]
        gas = 0
        for pump in actual_pumps:
            gas += pump
            # print(' ', pump, gas)
            if gas < 0:
                break
        if gas >= 0:
            return i

# truckTour(net_pumps)

def truckTour(petrolpumps):
    net_pumps = [pump[0]-pump[1] for pump in petrolpumps]
    # net_pumps = [3,-1,-1,-1,-1,2,2,-1,2]
    pos=0
    fuel=0
    for i in range(len(net_pumps)):
        fuel+=net_pumps[i]
        if fuel<0:
            pos=i+1
            fuel=0
    return pos

truckTour(petrolpumps)

arr = [3,-1,-1,-1,-1,2,2,-1,2]
n = len(arr)

# Step 1: Calculate prefix sums
prefix_sums = [0] * n
prefix_sums[0] = arr[0]
for i in range(1, n):
    prefix_sums[i] = prefix_sums[i-1] + arr[i]

# Step 2: Calculate suffix sums
suffix_sums = [0] * n
suffix_sums[-1] = arr[-1]
for i in range(n-2, -1, -1):
    suffix_sums[i] = suffix_sums[i+1] + arr[i]

# Step 3: Find the minimum index
# for i in range(n):
#     if prefix_sums[i] >= 0 and suffix_sums[i] >= 0:
#         print(i)
# return -1  # Return -1 if no such index exists


def findMinimumIndex(arr):
    n = len(arr)
    
    # Step 1: Calculate prefix sums
    prefix_sums = [0] * n
    prefix_sums[0] = arr[0]
    for i in range(1, n):
        prefix_sums[i] = prefix_sums[i-1] + arr[i]
    
    # Step 2: Calculate suffix sums
    suffix_sums = [0] * n
    suffix_sums[-1] = arr[-1]
    for i in range(n-2, -1, -1):
        suffix_sums[i] = suffix_sums[i+1] + arr[i]
    
    # Step 3: Find the minimum index
    for i in range(n):
        if prefix_sums[i] >= 0 and suffix_sums[i] >= 0:
            return i
    return -1  # Return -1 if no such index exists

# Example usage
arr = [3, -1, -1, -1, -1, 2, 2, -1, 2]
print(findMinimumIndex(arr))

    