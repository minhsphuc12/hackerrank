# Given a square grid of characters in the range ascii[a-z], rearrange elements of each row alphabetically, ascending. Determine if the columns are also in ascending alphabetical order, top to bottom. Return YES if they are or NO if they are not.

grid=['abc', 'ade', 'efg']

def gridChallenge(grid):
    # Write your code here

    sorted_grid = [sorted(x) for x in grid]
    n = len(grid[0])
    checking_grid = [[x[i] for x in sorted_grid] for i in range(n)]
    if all([x==sorted(x) for x in checking_grid]):
        return True
    return False        

[1,2,3].reverse()

# check_list = []
# for i in range(n):
#     print('i', i)
#     check_list.append([])
#     for x in sorted_grid:
#         print('x', x)
#         check_list[i].append(x[i])
