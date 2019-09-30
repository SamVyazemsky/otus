# Time Complexity: O(n²)
# Name: Quadratic
# Example operations: Find the shortest path between two nodes in a graph. Nested loops.

# Find target 22 (i.e. return its index) in a sorted list
# Here we use Binary Search algorithm because its time complexity is O(log n)


def binary_search(array, target):
    lower = 0
    upper = len(array)
    while lower < upper:   # use < instead of <=
        x = lower + (upper - lower) // 2
        val = array[x]
        if target == val:
            return x
        elif target > val:
            if lower == x:   # these two are the actual lines
                break        # you're looking for
            lower = x
        elif target < val:
            upper = x


print(binary_search([1, 3, 9, 22], 22))

# return 3
