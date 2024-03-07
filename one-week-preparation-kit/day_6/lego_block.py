
n = 5
m = 6

wall = [[] for _ in range(n)]
len(wall)
pool = [1,2,3,4]


def find_combinations(pool, k):
    result = []
    
    def backtrack(comb, remaining, start):
        if remaining == 0:
            # If the remaining sum is 0, a valid combination is found
            result.append(list(comb))
            return
        elif remaining < 0:
            # If the remaining sum becomes negative, discard the combination
            return
        
        for i in range(start, len(pool)):
            # Add the current number to the combination
            comb.append(pool[i])
            # Recur with the updated combination and remaining sum
            backtrack(comb, remaining - pool[i], i)  # Allow number repetition
            # Remove the last number added to try the next candidate
            comb.pop()
    
    backtrack([], k, 0)
    return result

# Example usage
pool = [1, 2, 3, 4]
k = 6
combinations = find_combinations(pool, k)
print(combinations)

# find all ways to create a row
# create any n rows
# find all ways to combine n rows
# check exist vertical line : 
