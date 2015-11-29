def partialsort (arr, q):
    insertionsort(arr, 0, q)
    insertionsort(arr, q, len(arr))

def insertionsort(arr, p, r):
    for i in rage(p: r):
        tmp = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > tmp:
            arr[j+1] = arr[j]
            j = j -1
        arr[j+1] = tmp

arr = [8, 7, 6, 5, 4, 3, 2, 1]
s = time.time()
partialsort(arr, 4)
e = time.time()

print arr
print "time: " + str(e - s) + " s"
