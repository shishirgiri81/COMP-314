from insertion_sort import insertionSort
from selection_sort import selectionSort

import numpy as np
import time

A = np.random.rand(10000)

begin = time.time()

result = insertionSort(A)

# result = selectionSort(A)

end = time.time()

print("Time Taken: ", end-begin)
