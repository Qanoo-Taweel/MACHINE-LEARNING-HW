# ==========================================
# Eigenvalues and Eigenvectors Homework
# ==========================================

# 1. THEORY (short explanation)
# Matrices are used to store data in machine learning.
# Eigenvectors represent directions in the data.
# Eigenvalues represent how important those directions are.
# They are used in PCA, dimensionality reduction, and feature extraction.

# ==========================================
# 2. CODE IMPLEMENTATION
# ==========================================

import numpy as np

# Define matrix
A = np.array([[4, 2],
              [1, 3]])

print("Matrix A:\n", A)

# ==========================================
# Manual eigenvalue calculation
# Characteristic equation: λ^2 - 7λ + 10 = 0
# ==========================================

manual_values = np.roots([1, -7, 10])

print("\nManual Eigenvalues:\n", manual_values)

# ==========================================
# NumPy eigenvalue calculation
# eig() returns eigenvalues and eigenvectors
# ==========================================

values, vectors = np.linalg.eig(A)

print("\nNumPy Eigenvalues:\n", values)
print("\nEigenvectors:\n", vectors)

# ==========================================
# 3. COMPARISON
# ==========================================

print("\nComparison:")
print("Manual and NumPy eigenvalues are approximately equal.")


