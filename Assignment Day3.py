import numpy as np
arr = np.array([[[1,2],[9,4]],[[5,6], [11,8]]])
print(np.sort(arr))


x = np.where(arr == (1,0))
print(x)
