# Time Complexity: O(n²)
# Name: Quadratic
# Example operations: Find the shortest path between two nodes in a graph. Nested loops.


def quadratic_algo(items):
    for item in items:
        for item2 in items:
            print(item, ' ' , item)


quadratic_algo([4, 5, 6, 8])
