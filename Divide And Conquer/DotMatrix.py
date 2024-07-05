# Το πρόβλημα του αποδοτικού πολλαπλασιασμού πινάκων
# Διαίρει και Βασίλευε- Μέθοδος Strassen
# για τη λύση
# Διαίρεσε το πίνακα σε 4 υποπίνακες
# Πολλαπλασίασε τους υποπίνακες αναδρομικά με τη μέθοδο Strassen
# Συνδύασε τα αποτελέσματα
# Πολυπλοκότητα: Θ(n^log7)
# ΥΓ: Καλά κρασιά
import numpy as np


def add_matrix(A, B):
    return np.add(A, B)


def sub_matrix(A, B):
    return np.subtract(A, B)


def strassen_multiply(A, B):
    n = len(A)

    # Base case: 1x1 matrix
    if n == 1:
        return A * B

    # Split matrices into quarters
    mid = n // 2
    A11 = A[:mid, :mid]
    A12 = A[:mid, mid:]
    A21 = A[mid:, :mid]
    A22 = A[mid:, mid:]

    B11 = B[:mid, :mid]
    B12 = B[:mid, mid:]
    B21 = B[mid:, :mid]
    B22 = B[mid:, mid:]

    # Calculate M1 to M7
    M1 = strassen_multiply(add_matrix(A11, A22), add_matrix(B11, B22))
    M2 = strassen_multiply(add_matrix(A21, A22), B11)
    M3 = strassen_multiply(A11, sub_matrix(B12, B22))
    M4 = strassen_multiply(A22, sub_matrix(B21, B11))
    M5 = strassen_multiply(add_matrix(A11, A12), B22)
    M6 = strassen_multiply(sub_matrix(A21, A11), add_matrix(B11, B12))
    M7 = strassen_multiply(sub_matrix(A12, A22), add_matrix(B21, B22))

    # Calculate C11, C12, C21, C22
    C11 = add_matrix(sub_matrix(add_matrix(M1, M4), M5), M7)
    C12 = add_matrix(M3, M5)
    C21 = add_matrix(M2, M4)
    C22 = add_matrix(sub_matrix(add_matrix(M1, M3), M2), M6)

    # Combine quarters into a single matrix
    C = np.zeros((n, n))
    C[:mid, :mid] = C11
    C[:mid, mid:] = C12
    C[mid:, :mid] = C21
    C[mid:, mid:] = C22

    return C


# Example usage
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
C = strassen_multiply(A, B)
print("Result of Strassen's multiplication:\n", C)
