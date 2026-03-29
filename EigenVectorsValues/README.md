# Eigenvalues and Eigenvectors in Machine Learning

## 1. Matrix Manipulation, Eigenvalues, Eigenvectors and ML

### Matrix Manipulation
In machine learning, data is usually stored in matrices. Each row represents a data sample, and each column represents a feature. Because of this, matrix operations like multiplication and transpose are very important in many algorithms.

### Eigenvalues and Eigenvectors
Eigenvectors can be thought of as directions in the data, while eigenvalues show how important these directions are.

Mathematically:
A * v = λ * v

Where A is a matrix, v is an eigenvector, and λ is the eigenvalue.

### Relationship with Machine Learning
Eigenvalues and eigenvectors are used in many machine learning techniques. One of the most important examples is PCA (Principal Component Analysis). PCA uses eigenvectors to find the most important directions in the data and reduce its size while keeping useful information.

They are also used in:
- dimensionality reduction
- feature extraction
- data compression

---

## 2. NumPy eig() Function

NumPy provides a function called:

numpy.linalg.eig()

This function takes a square matrix and returns its eigenvalues and eigenvectors.

Example:

```python
import numpy as np

A = np.array([[1,2],[3,4]])
values, vectors = np.linalg.eig(A)
```
---

## 3. Manual vs NumPy
Matrix used:
A = [[4, 2],
[1, 3]]
Manual calculation gives eigenvalues:
5 and 2
NumPy gives similar results.

---

## Conclusion

Eigenvalues and eigenvectors are very important in machine learning. They help understand data structure and are used in methods like PCA. 

---

## References

- https://machinelearningmastery.com/introduction-matrices-machine-learning/
- https://machinelearningmastery.com/introduction-to-eigendecomposition-eigenvalues-and-eigenvectors/
- https://numpy.org/doc/2.1/reference/generated/numpy.linalg.eig.html
- https://github.com/numpy/numpy/tree/main/numpy/linalg
- https://github.com/LucasBN/Eigenvalues-and-Eigenvectors

This work was implemented based on the provided resources and adapted for this assignment.

