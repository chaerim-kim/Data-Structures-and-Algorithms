# theres sorted & unsorted part of the array.
# find the element in the unsorted arr and select where in the sorted u would insert
# 앞쪽은 앞부분이 이미 정렬되어있다고 가정하 좀더 효율적

def insertionsort(arr):
    n = len(arr)

    for i in range(1,n):
        while arr[i-1] > arr[i] and i > 0:
            arr[i], arr[i-1] = arr[i-1],arr[i]
            # i 와 i-1을 비교하고, 그래도 작으면 i와 i-2 를 비교하기때문
            i = i-1

    return arr


print(insertionsort([7, 3, 2, 9, 4]))