# TO-DO: Complete the selection_sort() function below
'''
Consider the first element to be sorted and the rest to be unsorted
Assume the first element to be the smallest element.
Check if the first element is smaller than each of the other elements:
If yes, do nothing
If no, choose the other smaller element as minimum and repeat step 3
After completion of one iteration through the list, swap the smallest element with the first element of the list.
Now consider the second element in the list to be the smallest and so on till all the elements in the list are covered.
'''


def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):

        # store min value starting at index 0 to begin
        lowest = i

        # loop thru arr again starting at the index after lowest and keep looping until end of given arr
        for j in range(lowest + 1, len(arr)):
            # compare our next element to the current lowest element
            if arr[j] < arr[lowest]:
                # update our lowest var when the condition is met
                lowest = j

        # TO-DO: swap
        # Your code here
        # once we finish looping the second time we swap the original index with our lowest index found on that inner loop
        arr[i], arr[lowest] = arr[lowest], arr[i]

    return arr


# print(selection_sort([12, 9, 7, 40]))


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    for i in range(0, len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
    # OR #
    # for i in range(len(arr)-1, 0, -1):
    #     for j in range(i):
    #         if arr[j] > arr[i]:
    #             arr[i], arr[j] = arr[j], arr[i]
    return arr


# arr1 = [12, 7, 9, 44]
# print(bubble_sort(arr1))


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    # Your code here
    # counts will store the each variable in its own place
    # [0's, 1's, 2's, 3's, 4's...]
    counts = [0] * (maximum + 1)
    # loop thru the arr
    for i in arr:
        # print('counbts i', counts[i])
        # increment each index in order to count
        counts[i] += 1
        # print('counts', counts)

    num_items_before = 0
    for x, count in enumerate(counts):
        counts[x] = num_items_before
        num_items_before += count

    sorted_list = [None] * len(arr)

    for j in arr:
        sorted_list[counts[j]] = j
        counts[j] += 1

    return sorted_list


print(count_sort([2, 3, 3, 7, 5, 2], 7))
