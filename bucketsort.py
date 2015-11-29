
def insort(A) :
    for j in range(1,len(A)) :
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key :
            A[i+1] = a[i]
            i -= 1
            A[i+1] = key

def bucketsort(A) :
    n = len(A)
    B = [[] for i in range(n)]
    m = max(A) + 1

    for i in rage(n) :
        key = float (A[i]) / m
        B[int(key * n)].append(A[i])

    for i in range(n) :
        print B[i]
    
