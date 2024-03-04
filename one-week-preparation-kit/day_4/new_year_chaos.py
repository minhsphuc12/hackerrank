# It is New Year's Day and people are in line for the Wonderland rollercoaster ride. Each person wears a sticker indicating their initial position in the queue from 1 to n. Any person can bribe the person directly in front of them to swap positions, but they still wear their original sticker. One person can bribe at most two others.

# Determine the minimum number of bribes that took place to get to a given queue order. Print the number of bribes, or, if anyone has bribed more than two people, print Too chaotic.

q = [1,2,3,5,4,8,7,6]
# 1 2 5 3 7 8 6 4
q = [1,2,5,3,7,8,6,4]
q = [1,2,5,3,7,8,4,6]


q = [5,1,2,3,7,8,6,4]
q = [1,2,3,6,5,4,7,8]

q = [1,8,3,5,4,2,7,6]
q = [4,1,2,3]

init = list(range(1,len(q)+1))

q = [1,2,5,3,7,8,6,4]

def minimumBribes(q):
    bribes = 0
    # Start from the last person in the queue and move towards the first
    for i in range(len(q)-1, -1, -1):
        # Check if the current person has moved more than two positions
        if q[i] - (i + 1) > 2:
            print("Too chaotic")
            return
        # Count the number of people who overtook the current person
        # We only need to check up to two positions ahead of where
        # the person originally was, due to the problem constraints
        for j in range(max(0, q[i] - 2), i):
            if q[j] > q[i]:
                bribes += 1
                
    print(bribes)

# Example usage
q = [2, 1, 5, 3, 4]
minimumBribes(q)