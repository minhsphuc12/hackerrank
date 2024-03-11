k = 9 
l = A = [2,7,3,6,4,6]
A = [1,1,1]
[2,7,3,6,4,6].pop(0)

k = 90
A = [13, 47, 74, 12, 89, 74, 18, 38]

def cookies(k:int, A:list):
    def remove_min(l:list):
        index_min = l.index(min(l))
        return l.pop(index_min)
    stop = min(A) >= k
    step = 0
    while not stop and len(A) >= 2:
        min_cookie = remove_min(l=A)
        second_min_cookie = remove_min(A)
        new_cookie = min_cookie + 2 * second_min_cookie
        A.append(new_cookie)
        step += 1
        stop = min(A) >= k
    if not stop:
        return -1
    return step

cookies(k, A)

# faster algorithm

def cookies(k:int, A:list):
    import bisect
    def remove_min(l:list):
        return l.pop(0)
    A = sorted(A)
    stop = A[0] >= k
    step = 0
    while not stop and len(A) >= 2:
        min_cookie = remove_min(l=A)
        second_min_cookie = remove_min(A)
        new_cookie = min_cookie + 2 * second_min_cookie
        bisect.insort(A,new_cookie)
        step += 1
        stop = A[0] >= k
    if not stop:
        return -1
    return step

def cookies(k, A):
    # Convert A into a min-heap in-place; O(n) time complexity
    import heapq
    heapq.heapify(A)
    step = 0

    # Continue until the smallest element is at least k
    while len(A) > 1 and A[0] < k:
        # Remove the two smallest elements; O(log n) each
        min_cookie = heapq.heappop(A)
        second_min_cookie = heapq.heappop(A)

        # Combine the two cookies and add back to the heap; O(log n)
        new_cookie = min_cookie + 2 * second_min_cookie
        heapq.heappush(A, new_cookie)
        step += 1

    # After the loop, check if the condition is satisfied
    if A[0] < k:
        return -1  # Not possible to reach or exceed sweetness level k
    return step

cookies(k, A)