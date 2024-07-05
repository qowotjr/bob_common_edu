import random

def mergeSort(array):
    length = len(array)
    middle  = length//2
    if length == 1:
        return

    #middle 기준으로 쪼갤 두 개의 배열 생성
    leftarray = array[:middle]
    rightarray = array[middle:]

    #Divide, 하나의 배열을 middle 기준 두개로 쪼갬
    mergeSort(leftarray)
    mergeSort(rightarray)

    i = j = 0
    index = 0
    left_index = 0
    
    #Conquer, merge과정 값을 비교하여 작은값을 추가하고 index++
    while i<len(leftarray) or j<len(rightarray):
        if leftarray[i] > rightarray[j]:
            array[index] = rightarray[j]
            j+=1
        else:
            array[index] = leftarray[i]
            i+=1
        index+=1

        #왼쪽 배열이 다 정렬되면 남은 오른쪽 배열 정리
        if i==len(leftarray):
            left_index = len(rightarray)-j
            for k in range(left_index):
                array[index] = rightarray[j]
                j+=1
                index+=1
            break

        #오른쪽 배열이 다 정렬되면 남은 왼쪽 배열 정리
        elif j==len(rightarray):
            left_index = len(leftarray)-i
            for k in range(left_index):
                array[index] = leftarray[i]
                i+=1
                index+=1
            break

#길이가 100인 난수 배열 생성
array = []
for i in range(100):
    array.append(random.randrange(1,100))

#정렬 이전
print(array)
mergeSort(array)

#정렬 이후
print(array)