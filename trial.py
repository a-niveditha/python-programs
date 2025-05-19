'''def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        print(i,j)
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            print(arr," ",j)
        arr[j + 1] = key
    return arr

# Example usage:
arr = [12, 11, 13, 5, 6]
sorted_arr = insertion_sort(arr)
print("Sorted array:", sorted_arr)'''

'''def partitions_nk(n, k):
    if n == 0:
        return [[]]
    if n < 0 or k <= 0:
        return []

    exclude_partitions = partitions_nk(n, k - 1)
    include_partitions = partitions_nk(n - k, k)
    #print(include_partitions,exclude_partitions)

    new_partitions = []
    for p in include_partitions:
        new_partitions.append([k] + p)

    return exclude_partitions + new_partitions

def partitions(n):
    return partitions_nk(n, n)

print(partitions(5))'''

from math import log, ceil, floor
 
tests = int(input())
 
for _ in range(tests):
    k, l1, r1, l2, r2 = map(int, input().split())
    if (r2 < k * l1):
        print(0)
        continue
    min_n = max(0, ceil(log(l2/r1, k)))
    max_n = floor(log(r2/l1, k))
    if min_n > max_n:
        min_n, max_n = max_n, min_n
    count = 0
    for n in range(min_n, max_n + 1):
        power = k**n
        low = max(l1, ceil(l2/power))
        high = min(r1, floor(r2/power))
        count += max(0, high - low + 1)
    print(count)




 
