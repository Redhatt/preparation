# point to be NOTED
# 0 base index left child -> 2*i+1, right child -> 2*i+2 (i is parent)
# and parent -> (i-1)//2 (i is child)

from debug import debug

def left(i):
    return 2*i+1

def right(i):
    return 2*i+2

def valid(i, n):
    return (left(i)<=n-1), (right(i)<=n-1)

def verify(heap):
    n = len(heap)
    for i in range(n):
        l,r = valid(i, n)
        if r:
            if heap[right(i)]<heap[i]:
                print(False)
                debug(root=f"{i} -> {heap[i]}", c___=f"{right(i)} -> {heap[right(i)]}", child="right")
                return False
        if l:
            if heap[left(i)]<heap[i]:
                print(False)
                debug(root=f"{i} -> {heap[i]}", c___=f"{left(i)} -> {heap[left(i)]}", child="left")
                return False
    print(True)
    return True


def insert(heap, data):
    heap.append(data)
    n = len(heap)
    i = n-1
    while heap[i]<heap[i//2] and i!=0:
        heap[i], heap[i//2] = heap[i//2], heap[i]
        i = i//2

def delete(heap):
    if heap:
        val = heap[0]
        heap[0] = heap[-1]
        heap.pop()
        n = len(heap)
        i = 0
        while(i<n):
            l,r = valid(i, n)
            if r:
                index = left(i) if heap[left(i)]<=heap[right(i)] else right(i)
                if heap[i]>heap[index]:
                    heap[i], heap[index] = heap[index], heap[i]
            elif l:
                index = left(i)
                if heap[i]>heap[index]:
                    heap[i], heap[index] = heap[index], heap[i]
            else:
                break
            i = index
        return val
    else:
        return None


def insertion_arr(arr):
    n = len(arr)
    for j in range(1,n):
        i = j
        while arr[i]<arr[i//2] and i!=0:
            arr[i], arr[i//2] = arr[i//2], arr[i]
            i = i//2
        # debug(i=i, arr=arr)

def heapify(arr):
    n = len(arr)
    for i in range(n):
        l,r = valid(i, n)
        if l and r:
            index = left(i) if arr[left(i)]<=arr[right(i)] else right(i)
            if arr[i]>arr[index]:
                arr[i], arr[index] = arr[index], arr[i]
        elif l:
            index = left(i)
            if arr[i]>arr[index]:
                arr[i], arr[index] = arr[index], arr[i]
        elif r:
            index = right(i)
            if arr[i]>arr[index]:
                arr[i], arr[index] = arr[index], arr[i]

arr = [50, 3, 10, 93, 48, 94]

insertion_arr(arr)
print(arr)
verify(arr)

# insert(arr, 7)
# print(arr)
# verify(arr)

print(delete(arr))
print(arr)
verify(arr)

# t = []
# insert(t, 0)
# print(t)
