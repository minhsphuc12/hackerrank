from itertools import product
from itertools import permutations, combinations
from tqdm import tqdm
from pprint import pprint

n = 4
m = 4
def legoBlocks(n, m):
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
    brick_combinations = find_combinations(pool, m)
    print(brick_combinations)

    # find all ways to create a row
    # create any n rows
    rows = [list(set(list(permutations(combination)))) for combination in brick_combinations]
    rows = [list(i) for x in rows for i in x]
    # find all ways to combine n rows
    all_walls = list(product(rows, repeat=n))
    
    # check exist vertical line:
    len(all_walls)
    pprint(all_walls)
    all_walls[300]

    def check_gap(wall):
        gap_count = {k:0 for k in range(1, m)}
        for row in wall:
            gap = 0
            for brick in row:
                gap += brick
                if gap != m:
                    gap_count[gap] += 1
        return len(list(filter(lambda x: gap_count[x]==n, gap_count))) > 0

    valid_wall = 0
    for wall in tqdm(all_walls):
        if not check_gap(wall):
            valid_wall += 1
            print(wall)

    return valid_wall


def legoBlocks(n, m):
    # Step 1: Count ways to build a single row
    single_row_ways = [0] * (m + 1)
    single_row_ways[0] = 1
    for width in range(1, m + 1):
        print('width', width)
        for block_width in [1, 2, 3, 4]:
            print(' block_width', block_width)
            if width >= block_width:
                single_row_ways[width] += single_row_ways[width - block_width]
                print('    ', single_row_ways)
    
    # Step 2: Calculate total ways to build the wall of height n
    total_ways = [pow(ways, n) for ways in single_row_ways]

    # Step 3: Calculate valid ways using inclusion-exclusion principle
    valid_ways = [0] * (m + 1)
    for width in range(1, m + 1):
        valid_ways[width] = total_ways[width]
        for k in range(1, width):
            valid_ways[width] -= valid_ways[k] * total_ways[width - k]
    
    # Modulo 10**9 + 7 is usually required to prevent integer overflow in programming contests
    return valid_ways[m] % (10**9 + 7)


def legoBlocks(n, m):
    mod = 1000000007

    # Step 1: Calculate ways to fill a row
    row_ways = [1] + [0]*m
    for width in range(1, m + 1):
        for block in [1, 2, 3, 4]:
            if width >= block:
                row_ways[width] = (row_ways[width] + row_ways[width - block]) % mod

    # Step 2: Calculate total and invalid ways
    total_ways = [pow(w, n, mod) for w in row_ways]
    valid_ways = total_ways[:]

    for width in range(1, m + 1):
        for k in range(1, width):
            valid_ways[width] -= valid_ways[k] * total_ways[width - k]
            valid_ways[width] %= mod

    return valid_ways[m]


legoBlocks(2,2)
legoBlocks(271, 700)
legoBlocks(4,4)
legoBlocks(2,2)
legoBlocks(2,2)


