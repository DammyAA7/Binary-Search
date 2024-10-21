def binary_search(arr, target):
    left = 0 # left pointer
    right = len(arr) - 1 # right pointer

    while left <= right: # while left pointer is less than or equal to right pointer
        mid = (left + right) // 2 # find the middle index
        mid_val = arr[mid] # find the middle value

        if mid_val == target: # if the middle value is equal to the target
            return mid # return the index of the target
        elif mid_val > target:
            right = mid - 1 # if the middle value is greater than the target, move the right pointer to the left
        else:
            left = mid + 1 # if the middle value is less than the target, move the left pointer to the right
    return None