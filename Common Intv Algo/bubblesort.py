# [7, 3, 2, 9, 4]가 들어있는 배열을 오름차순으로 정렬해서 리턴하는 함수를 만들고 주어진 배열을 정렬하세요.
# 뒷 아이템에서 부터 하나씩 소팅되기때문에 그 거를 n-i-1으로 줄여나감


# O(n2) solution
def bubblesort(arr):
    n = len(arr)
    for i in range (n):
        for j in range ( n-i-1):        #뒤에서부터하나식 줄어들기때문
            # print(arr[i], arr[j])
            # print(i,j)

            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

print(bubblesort([10, 7, 3, 2, 9, 4]))