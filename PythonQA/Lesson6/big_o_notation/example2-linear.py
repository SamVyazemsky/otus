# Time Complexity: O(n)
# Name: Linear
# Example operations: copy, insert, delete, iteration.
# First algoritm


def linear_algo(items):
    for item in items:
        print(item)


linear_algo([4, 5, 6, 8])
# Linear search algorithm
# Find target 22 (i.e. return its index)in a sorted list


def linearSearch(sortedList, target):
    for i in range(len(sortedList)):
        if sortedList[i] == target:
            return i
# If target is not in the list, return -1
    return -1


print(linearSearch([1, 3, 9, 22], 22))



import matplotlib.pyplot as plt
import numpy as np

x = [2, 4, 6, 8, 10, 12]

y = [2, 4, 6, 8, 10, 12]

plt.plot(x, y, 'b')
plt.xlabel('Inputs')
plt.ylabel('Steps')
plt.title('Linear Complexity')
plt.show()