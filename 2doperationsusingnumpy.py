import numpy as np
a = np.ndarray(shape=(3,3), dtype=int)
a[0][0]=1
a[0][1]=2
a[0][2]=3
a[1][0]=4
a[1][1]=5
a[1][2]=6
a[2][0]=7
a[2][1]=8
a[2][2]=9
print("matrix1 elements are: \n",a)
print("dimension of matrix1 is: ",a.ndim)
b=np.ndarray(shape=(3,3), dtype=int)
b[0][0]=1
b[0][1]=3
b[0][2]=5
b[1][0]=7
b[1][1]=9
b[1][2]=11
b[2][0]=13
b[2][1]=15
b[2][2]=17
print("matrix2 elemnts are: \n",b)
print("dimension of matrix2 is: ",b.ndim)
print("addition of two matrixes are: \n",np.add(a,b))
print("subtraction of two matrixes are: \n",np.subtract(a,b))
print("corresponding multiplication of two matrices are: \n",np.multiply(a,b))
print("Divison of two matrixes are: \n",np.divide(a,b))
print("matrix multplication of two matrices are: \n",np.dot(a,b))
