# 반복적으로 한개가 남을때까지 n/2로 나눈다 - conquer
# 그후, 나뉜 두 리스트의 앞부분 부터 비교하며 반복적으로 merge한


def mergesort(arr):
    # if the list has more than 1 element (not sorted)
    if len(arr)<= 1: return arr

    mid = len(arr) // 2

    # split the array
    L = mergesort(arr[:mid])
    R = mergesort(arr[mid:])

    return merge(L,R)


def merge(L,R):
    result = []
    i = j = 0

    # now merge it to real
    while len(L) > i and len(R) >j:
        #  앞쪽배열이 더 클때
        if L[i] < R[j]:
            result.append(L[i])
            i = i+1
        else:
            result.append(R[j])
            j = j+1

    # 남은 값이 있다면 append
    while i < len(L):
        result.append(L[i])
        i+=1

    # 앞쪽 배열에 남았으면
    while j < len(R):
        result.append(R[j])
        j+=1

    return result



print(mergesort([7, 3, 2, 9, 4]))