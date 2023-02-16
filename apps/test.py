import numpy as np

data = [1,2,3,4,5,6,7,8,9,10]

# print(np.std(data))

b = np.array(data)
print(type(b))


arr = np.array([[1, 2, 3], [14, 5, 6]])
print(arr[0:2, len(arr)-1:])