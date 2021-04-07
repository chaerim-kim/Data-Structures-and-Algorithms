# 제일 미니멈을 찾고, 미니멈을 어레이의 맨 앞과 계속 교체.


def selectionsort(arr):
    n = len(arr)

    for i in range(n):
        mini = i
        for j in range (i+1, n):
            if arr[j] < arr[mini]:
                mini = j

        # if the order changed
        if mini != i:
            arr[mini],arr[i] = arr[i], arr[mini]

    return arr


print(selectionsort([7, 3, 2, 9, 4]))