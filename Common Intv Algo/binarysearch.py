# array must be sorted. u compare the target with midpoint and u halve it
def binary_search(arr, target):
    return recursive(arr, target, 0, len(arr)-1)



def recursive(arr, target, L, R):
    if L <= R:
        mid = (L+R) // 2

        if arr[mid] == target:
            return mid

        # If element is smaller than mid, then it will be present in left subarray
        elif target < arr[mid]:
            return recursive(arr, target, L, mid-1)

        else:
            return recursive(arr, target, mid+1, R)

    else:
        return False


print(binary_search([1,4,5,6,7,8,9], 7))