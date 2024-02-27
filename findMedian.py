def get_med(arr):
    # arr = [1,3,5,76,32,5,3]
    sorted_arr = sorted(arr)
    length = len(arr)
    if length % 2 == 1:
        median = sorted_arr[int((length-1)/2)]
    if length % 2 == 0:
        median = sorted_arr[int(length/2)]
    return median
