import numpy as np
import copy


def swap_columns(a, i, j):
  for k in range(len(a)):
    a[k][i], a[k][j] = a[k][j], a[k][i]


def swap_row(a, i, j):
  temp = copy.copy(A[i])
  A[i] = A[j]
  A[j] = temp


def print_array(A):
  for i in range(0, len(A), 1):
    for j in range(0, len(A[i]), 1):
      print("%.4f     " % A[i][j], end="")
    print("")


#прямой ход решения
def decision_sle_direct_move(A):
  for k in range(0, 4, 1):
    # вернём индекс максимального элемента по модулю из столбца
    index_max = np.argmax(abs(A[k:, k])) + k
    #меняем строки местами
    swap_row(A, k, index_max)

    A[k] /= A[k][k]
    for i in range(k + 1, n, 1):
      A[i] = A[i] - A[k] * A[i][k]
  return A


#обратный ход, нахождение X
def decision_sle_reverse_move(A, X, F):
  X[n - 1] = F[n - 1]
  for k in reversed(range(0, n - 1, 1)):
    sum_row = 0
    for i in reversed(range(0, n, 1)):
      if (A[k][i] == 0.0):
        continue
      if (X[i] is not None):
        sum_row += A[k][i] * X[i]
    X[k] = F[k] - sum_row
  return X


A_orig = np.array([(3.25, 1.54, 4.91, 2.43), (-3.34, 1.17, 3.2, 5.13),
                   (-9.52, 2.73, 3.37, -5.89), (1.13, 2.21, 4.47, 5.11)])

A = copy.copy(A_orig)
F = np.array([0.14, 1.15, 0.92, 5.65])
X = np.array([None, None, None, None])

n = len(A)

# прямой ход
A = np.column_stack((A, F))
A = decision_sle_direct_move(A)
print("Полученная трапецевидная (расширенная) матрица A:")
print_array(A)

F = A[:, 4]
A = A[:, :4]
# обратное ход
X = decision_sle_reverse_move(A, X, F)
print("\nПолученное решение:", end="")
print("\n\nX = ", X, "\n\n")

#вектор невязки
r = np.dot(A, X) - F
print("Вектор невязки: ", r, "\n\n")

#определитель
L = copy.copy(A_orig)

pivot_index = -1
pivot_value = 0
determinant = 1

for i in range(0, n, 1):
  index_max = np.argmax(abs(A[i:, i])) + i
  swap_row(L, index_max, i)
  determinant *= -1  #меняем знак
  for j in range(i + 1, n, 1):
    multiplier = 1 / L[i][i] * L[j][i]
    for k in range(i, n, 1):
      L[j][k] -= L[i][k] * multiplier
  determinant *= L[i][i]

print("Детерминант = ", determinant)

E = []
E.append(np.array([1, 0, 0, 0]))
E.append(np.array([0, 1, 0, 0]))
E.append(np.array([0, 0, 1, 0]))
E.append(np.array([0, 0, 0, 1]))

A_reverse = np.empty((4, 0), dtype=float)

for i in range(0, 4, 1):
  B = copy.copy(A_orig)
  B = np.column_stack((B, E[i]))  #создаём расширенную матрицу
  B = decision_sle_direct_move(B)  #прямой ход решения

  #
  # Разбиваем полученную расширенную матрицу обратно на матрицу и вектор
  #
  E[i] = copy.copy(B[:, 4])
  B = copy.copy(B[:, :4])

  A_reverse_temp = np.array([None, None, None, None])  #временное хранение
  A_reverse_temp = decision_sle_reverse_move(B, A_reverse_temp,
                                             E[i])  #обратный ход, ищем решение
  A_reverse = np.column_stack(
    (A_reverse, A_reverse_temp))  #собираем обратную матрицу

print("\n Обратная матрица А:")
print_array(A_reverse)

print("\n Проверка А*A_inv:")
print_array(np.dot(A_orig, A_reverse))
