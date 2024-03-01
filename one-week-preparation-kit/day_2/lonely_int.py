def lonelyinteger(a):
    # Write your code here
    a = [1,2,2,3,4,4,1]
    from collections import Counter
    counter = Counter(a)
    filtered_dict = {key: value for key, value in counter.items() if value == 1}
    return list(filtered_dict)[0]
