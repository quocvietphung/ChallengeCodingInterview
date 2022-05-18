import numpy as np
a = np.array([1, 2, 3]) # T¤o array 1 chi·u
print(type(a)) # Prints "<class 'numpy.ndarray'>"
print(a.shape) # Prints "(3,)"
print(a[0], a[1], a[2]) # Prints "1 2 3"
a[0] = 5
print(a)
b = np.array([[1,2,3],[4,5,6]])
print(b.shape) # Prints "(2, 3)"
print(b[0, 0], b[0, 1], b[1, 0]) # Prints "1 2 4"
a = '1234'
print (a[::-2])
