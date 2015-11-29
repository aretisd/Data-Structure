import time

def trace(a, start, end):
    #print "----- siftdown ----"
    #print "start = " + str(start)
    #print "end = " + str(end)
    print a


def siftdown(a, start, end):
    root = start

    while root * 2 + 1 <= end:
        child = root *2 + 1
        swap = root

        #check the "root" against the left child
        if a[swap] < a[child]:
            swap = child

        #check the "root" against the right child
        if child + 1 <= end and a[swap] < a[child+1]:
            swap = child + 1

        #swap the largest child with the "root"
        if swap == root:
            trace(a, start, end)
            return
        else:
            tmp = a[root]
            a[root] = a[swap]
            a[swap] = tmp
            root = swap
            trace(a, start, end)
        


def heapify(a, count):
    start = (count - 2) / 2
    while start >= 0:
        #print "----- heapify ------"
        #print "start = " + str(start)
        #print "count = " + str(count)
        #print a
        siftdown(a, start, count-1)
        start = start - 1

def heapsort(a, count):
    heapify(a, count)

    end = count - 1
    while end > 0:
        tmp = a[0]
        a[0] = a[end]
        a[end] = tmp
        end = end -1
        siftdown(a, 0, end)




n = input("n = ")
a = [i for i in range(n)]

s = time.time()
heapsort(a, n)
e = time.time()

print a
print "time: " + str(e - s) + " s"


