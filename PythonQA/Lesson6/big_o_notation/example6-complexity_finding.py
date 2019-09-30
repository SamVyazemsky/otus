def complex_algo(items):
    # The complexity of this part is O(5)
    for i in range(5):
        print("Python is awesome")
    # The complexity of the following piece of code is also O(n)
    for item in items:
        print(item)
    # The complexity of the following piece of code is also O(n)
    for item in items:
        print(item)
    # The following piece of code, a string is being printed three times, hence the complexity is O(3)
    print("Big O")
    print("Big O")
    print("Big O")


complex_algo([4, 5, 6, 8])
# Total:
# O(5) + O(n) + O(n) + O(3) = O(8) + O(2n)
