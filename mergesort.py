import random

def mergeSort(array):
    length = len(array)
    middle  = length//2
    if length == 1:
        return
    leftarray = array[:middle]
    rightarray = array[middle:]
    mergeSort(leftarray)
    mergeSort(rightarray)
    i = j = 0
    index = 0
    left_index = 0
    while i<len(leftarray) or j<len(rightarray):
        if leftarray[i] > rightarray[j]:
            array[index] = rightarray[j]
            j+=1
        else:
            array[index] = leftarray[i]
            i+=1
        index+=1
        if i==len(leftarray):
            left_index = len(rightarray)-j
            for k in range(left_index):
                array[index] = rightarray[j]
                j+=1
                index+=1
            break
        elif j==len(rightarray):
            left_index = len(leftarray)-i
            for k in range(left_index):
                array[index] = leftarray[i]
                i+=1
                index+=1
            break

array = []
for i in range(100):
    array.append(random.randrange(1,100))

print(array)
mergeSort(array)
print(array)