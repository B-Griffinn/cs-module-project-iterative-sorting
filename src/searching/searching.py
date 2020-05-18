def linear_search(arr, target):
    # Your code here
    for i in range(0, len(arr)):
        if arr[i] == target:
            return i

    return -1


# print(linear_search([1, 4, 7, 9, 3], ))

# Write an iterative implementation of Binary Search


def binary_search(arr, target):

    # Your code here
    # we need a l, r, and middle
    left = 0
    right = len(arr) - 1
    middle = len(arr) // 2

    # while our left is <= right loop thru the list
    while left <= right:
        middle = (left + right) // 2
        found = arr[middle]

        if found == target:
            return middle
        elif found < target:
            left = middle + 1
        elif found > target:
            right = middle - 1

    # return -1  # not foun/d
    return -1


print(binary_search([0, 1, 2, 3, 5, 7, 8], 1))
