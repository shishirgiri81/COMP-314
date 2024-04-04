from insertion_sort import insertionSort
from selection_sort import selectionSort

import numpy as np
import time
import matplotlib.pyplot as plt
import matplotlib as mpl



def main():

    A = np.random.rand(100)

    x = [100 , 1000, 10000, 100000, 1000000]
    n = len(x)

    y_insertionSort = []
    y_selectionSort = []

    for i in range(0, n):

        begin = time.time()

        result = insertionSort(A)

        end = time.time()

        y_insertionSort[i] = end - begin

        begin = time.time()

        result = insertionSort(A)

        end = time.time()

        y_selectionSort[i] = end - begin

    plt.plot(x, y_insertionSort, label = 'Insertion Sort')
    plt.plot(x, y_selectionSort, label = 'Selection Sort')
    plt.xlabel('Array Size(n)')
    plt.ylabel('Time(sec)')
    plt.title('Insertion Sort Vs Selection Sort')
    plt.legend()
    plt.show()

if __name__ == '__main__':
    main()








