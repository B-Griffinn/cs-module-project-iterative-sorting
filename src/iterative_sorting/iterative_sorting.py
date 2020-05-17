# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr)):
        # store min value
        lowest = i

        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        for j in range(lowest + 1, len(arr)):
            # print(lowest, j)
            if arr[j] < arr[lowest]:
                lowest = j

            # TO-DO: swap
            # Your code here
        arr[i], arr[lowest] = arr[lowest], arr[i]
    return arr


print(selection_sort([12, 9, 7, 40]))


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    # Your code here

    return arr
