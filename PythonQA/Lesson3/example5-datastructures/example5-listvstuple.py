import sys
l = list(range(int(1E9)))
t = tuple(list(range(int(1E9))))
sys.getsizeof(l)  # 90000120
sys.getsizeof(t)  # 80000056