def sort(arr,q):
    p = q
    r = len(arr)
    q = (p + r)/2
    if q == 0 :       
        merge(arr,p,q,r)
    else:
        arr = arr + merge(arr,p,q,r)
        

def mergesort(arr, p, r):
    if p + 1 < r:
        q = (p + r)/2
        mergesort(arr,p,q)
        mergesort(arr,q,r)
        merge(arr,p,q,r)


    
def merge(arr,p,q,r):
    
    i = p
    j = q
    result = []
    while i < q and j < r:
        if arr[i] < arr[j]:
            result.append(arr[i])
            i = i + 1
           
        else:
            result.append(arr[j])
            j = j + 1

    arr[p:r] = result + arr[i:q] + arr[j:r]
    

arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
sort(arr,1)
print(arr)


