def sort(arr):
    lowest = arr[0] #Stores the lowest value.
    lowest_index = 0 #Stores the index of lowest value.
    for i in range(1, len(arr)):
        if arr[i] < lowest:
            lowest = arr[i] #Updates the newest value.
            lowest_index = i #Updates the index for the current lowest value.
    return lowest_index
def selection_sort(arr):
    newArr = [] #Creates a new array.
    for i in range(len(arr)): #Finds the smallest element in the array and adds it to the new array.
        lowest = sort(arr)
        newArr.append(arr.pop(lowest))
    return newArr

print (selection_sort([5, 3, 6, 2, 10]))