import numpy as np

# list1 = [1, 2, 3]

# np1 = np.array([1, 2, 3])
# np2 = np.array([1.0, 2, 3])
# np3 = np.array(range(1, 4))
# np4 = np.array([range(x, x+3) for x in [2, 4, 6]])

# np5 = np.zeros(10, dtype=np.int)
# np6 = np.ones(10, dtype=np.int)
# np7 = np.ones((3, 5), dtype=np.int)
# np8 = np.full((3, 5), 255)
# np9 = np.arange(0, 20, 2)
# np10 = np.linspace(0, 1, 5)
# np11 = np.random.random((3, 3))
# np12 = np.random.randint(1, 6, (3, 3))
# np13 = np.random.normal(0, 1, (3, 3))
# np14 = np.eye(7)
# np15 = np.empty(7)

list1 = [1, 2, 3, 4, 5, 6, 7]
list2 = list1[1:4]
print(list2)
list2[0] = 100
print(list1)

np1 = np.array([1, 2, 3, 4, 5, 6, 7])
np2 = np1[1:4]
print(np2)
np2[0] = 1000
print(np1)

# print(list1)
# print(np1)
# print(np2)
# print(np3)
# print(np4)