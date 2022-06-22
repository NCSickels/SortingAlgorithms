import random,time

array = [54, 73, 84, 2, 98, 45, 48, 68, 52, 16]

def Sort(array, method):

    if method.lower() == 'bubble':
        print("Bubble Sort selected.")
        #bubble match lets go bois
        print(array)
        comparisons = 0
        for i in range(len(array) - 1):
            for j in range(len(array) - i):
                comparisons += 1
                if j > 0:
                    if array[j-1] > array[j]:
                        temp = array[j]
                        array[j] = array[j-1]
                        array[j-1] = temp
        print(array, 'with', comparisons, 'comparisons.')
    
    elif method.lower() == 'quick':
        print("Quick Sort selected.")
        def quick_sort(array, start, end): 
            def partition(array, start, end):
                pivot = array[start]
                low = start + 1
                high = end
                while True: 
                    while low <= high and array[high] >= pivot: 
                        high -= 1
                    while low <= high and array[low] <= pivot: 
                        low += 1
                    if low <= high: 
                        array[low], array[high] = array[high], array[low]
                    else: 
                        break
                array[start], array[high] = array[high], array[start]
                return high
            if start >= end: 
                return
            p = partition(array, start, end)
            quick_sort(array, start, p-1)
            quick_sort(array, p+1, end)
        quick_sort(array, 0, len(array) - 1)
        print(array)
        
    # Fix Selection Sort
    elif method.lower() == 'selection': 
        print("Selection Sort selected.")
        def selectionSort(array): 
            def findMinIndex(array, start): 
                min_index = start 
                start += 1
                while start < len(array): 
                    if array[start] < min_index: 
                        min_index = start
                    start += 1
                return min_index
            i = 0
            while i < len(array): 
                min_index = findMinIndex(array, i)
                if i != min_index: 
                    array[i], array[min_index] = array[min_index], array[i]
                i += 1
            print(array)
        selectionSort(array)

    elif method.lower() == 'merge': 
        print("Merge Sort selected.")
        def mergeSort(array): 
            if len(array) > 1: 
                mid = len(array) // 2
                left = array[:mid]
                right = array[mid:]
                mergeSort(left)
                mergeSort(right)
                i = j = k = 0
                while i < len(left) and j < len(right): 
                    if left[i] < right[j]: 
                        array[k] = left[i]
                        i += 1
                    else: 
                        array[k] = right[j]
                        j += 1
                    k += 1
                while i < len(left): 
                    array[k] = left[i]
                    i += 1
                    k += 1
                while j < len(right): 
                    array[k] = right[j]
                    j += 1
                    k += 1
            print(array)
        mergeSort(array)

    elif method.lower() == 'insertion': 
        print("Insertion Sort selected.")
        comparisons = 0
        for i in range(1, len(array)): 
            key = array[i]
            j = i - 1
            while j >= 0 and key < array[j]: 
                array[j+1] = array[j]
                j -= 1
                array[j+1] = key
                comparisons += 1
        print(array, 'with', comparisons, 'comparisons.')

    elif method.lower() == 'random':
        print('Random Sort selected.')
        startTime = time.time()
        comparisons = 0
        while True:
            randomSlots = []
            newArr = []
            usableSlots = list(range(len(array)))
            for num in array:
                slot = random.randint(0,len(usableSlots)-1)
                randomSlots.append(usableSlots[slot])
                usableSlots.pop(slot)
            for num in randomSlots:
                newArr.append(array[num])
            #print(newArr)
            #verify the num is in order
            inOrder = True
            for i in range(len(newArr)):
                comparisons += 1
                if i >0 and newArr[i] < newArr[i-1]:
                    inOrder = False
                    break
            comparisons += 1
            if inOrder: break
        print('its finally in order!',newArr)
        print('it took: ',time.time()-startTime)
        print('comparisons: ',comparisons)

method = input("Which sorting method do you want to use? ")
Sort(array, method)

