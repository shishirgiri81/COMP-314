import random

def selectionSort(A):
    n = len(A)

    for i in range(0, n-1):
        min = i
        
        for j in range(i+1, n):
            if A[j] < A[min]:
                min = j
        
        temp = A[i]
        A[i] = A[min]
        A[min] = temp

    # return A

A = [random.randint(1, 100) for _ in range(10)]