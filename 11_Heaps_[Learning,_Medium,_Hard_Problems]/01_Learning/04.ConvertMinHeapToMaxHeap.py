#https://www.naukri.com/code360/problems/convert-min-heap-to-max-heap_1381084

from typing import List


def minToMaxHeap(n: int, arr: List[int]) -> List[int]:
    # Start from the last non-leaf node down to the root node (0)
    for i in range((n - 2) // 2, -1, -1):
        curr = i

        # Iterative Max-Heapify
        while True:
            left = 2 * curr + 1
            right = 2 * curr + 2
            largest = curr

            # Check if left child exists and is greater than current
            if left < n and arr[left] > arr[largest]:
                largest = left

            # Check if right child exists and is greater than current largest
            if right < n and arr[right] > arr[largest]:
                largest = right

            # If the current node is already the largest, heap property holds
            if largest == curr:
                break

            # Swap current node with the larger child and continue down
            arr[curr], arr[largest] = arr[largest], arr[curr]
            curr = largest

    return arr
