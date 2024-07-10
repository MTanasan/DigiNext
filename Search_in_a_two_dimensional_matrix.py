# Python Program for recursive binary search. 
def flatten_extend(matrix):
    flat_list = []
    for row in matrix:
        flat_list.extend(row)
    return flat_list  

def binarySearch (arr, l, r, x): 

    if r >= l: 
        mid = l + (r - l)//2
        if arr[mid] == x: 
            return True 

        elif arr[mid] > x: 
            return binarySearch(arr, l, mid-1, x) 

        else: 
            return binarySearch(arr, mid + 1, r, x) 
        
    else: 
        return False
arr = [[1, 3, 5], [7, 8, 10], [12, 15, 18]]
flatten_arr = flatten_extend(arr)
x=3
result = binarySearch(flatten_arr, 0, len(flatten_arr)-1, x) 
print(result)