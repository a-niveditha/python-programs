def insertion_sort(arr):
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
print("Sorted array:", sorted_arr)


 
