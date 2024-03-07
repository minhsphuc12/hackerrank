k = 2
arr = [1,2,3,4,5,5,5,6,7,8,8,9]

arr = [1, 5, 3, 4, 2]

def pairs(k, arr):
    if len(arr) <= 1:
        return 0
    
    using_array = sorted(arr, reverse=True) if k >= 0 else arr

    result = 0
    for i in range(len(using_array)-1):
        for j in range(i+1, len(using_array)):
            print(i, j)
            # print(using_array[i], using_array[j])
            if using_array[i] - using_array[j] < k:
                pass
            elif using_array[i] - using_array[j] == k:
                result += 1
                print('hit')
            else: 
                'ignore rest'
                break
    return result

pairs(k, arr)
list(range(0,3))
for i in range(10):
    print(i)
    if i == 5:
        break