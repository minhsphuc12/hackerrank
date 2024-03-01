# Two players are playing a game of Tower Breakers! Player 1 always moves first, and both players always play optimally.The rules of the game are as follows:

# Initially there are  towers.
# Each tower is of height .
# The players move in alternating turns.
# In each turn, a player can choose a tower of height  and reduce its height to , where  and  evenly divides .
# If the current player is unable to make a move, they lose the game.
# Given the values of  and , determine which player will win. If the first player wins, return . Otherwise, return .

# Sample Input

# STDIN   Function
# -----   --------
# 2       t = 2
# 2 2     n = 2, m = 2
# 1 4     n = 1, m = 4
# Sample Output

# 2
# 1
# Explanation

def towerBreakers(n, m):
    if m==1 or n%2==0:
        return 2
    return 1

# Here's an explanation for some posted solutions.

# In the edge case (m=1) Player 1 cannot move and Player 2 wins.

# Now suppose (m > 1) and that we have an even number of towers (n % 2 == 0) . Player 1 can take some tower and reduce it to some divisor, which can be 1 or greater than 1. Player 2 can simply take another tower and match Player 1's move. Because there are an even number of towers, Player 2 will keep matching Player 1's moves until Player 1 can only reduce a tower to the divisor 1 (which Player 2 will match) and so Player 1 will be left with only towers of height 1, making Player 2 win.

# If we have an odd number of towers (n % 2 == 1) Player 1 can reduce one tower to 1, meaning that Player 2 now has an even number of non-1 towers, and from before Player 2 must lose. Thus Player 1 wins.
