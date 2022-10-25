import numpy as np
import copy

def swap_columns(a, i, j):
  for k in range(len(a)):
    a[k][i], a[k][j] = a[k][j], a[k][i]

def swap_row(a, i, j):
  temp =  copy.copy(A[i])
  A[i] = A[j]
  A[j] = temp

A_orig = np.array([(3.25, 1.54, 4.91, 2.43),
              (-3.34, 1.17, 3.2, 5.13),
              (-9.52, 2.73, 3.37, -5.89),
              (1.13, 2.21, 4.47, 5.11)])

A = A_orig
F = np.array([0.14, 1.15, 0.92, 5.65])
X = np.array([None, None, None, None])

n = len(A)
# print(n)
# print(A,"\n\n")
# for index in range(0, n, 1):
#   index_max = np.argmax(abs(A[:,index]))
#   swap_row(A, index, index_max)
  # print(A,"\n")
# index_max = np.argmax(abs(A[0]))
# print(index_max)

# swap_columns(A, k, index_max)
# print(A)


# index_max = np.argmax(abs(A[1:,1]))
# print("index=", index_max, " ", A[1:,1])
# B =  np.array([0.21220588, 2.47198529, 2.53404412])
# index_max = np.argmax(B)
# print("index=", index_max, " ", B)
# exit()

# прямой ход
A = np.column_stack((A, F))
print("Трапецевидная (расширенная) матрица A:\n\n",A,"\n")
for k in range(0, 4, 1):
  # вернём индекс максимального элемента по модулю из столбца
  index_max = np.argmax(abs(A[k:,k])) + k
  # print(A[index_max][k],"  ", abs(A[k:,k]))
  #меняем строки местами
  swap_row(A, k, index_max)
  # print(A,"\n") 
  A[k] /= A[k][k]
  for i in range(k+1, n, 1):
      A[i] = A[i] - A[k] * A[i][k]
    
print("Полученная трапецевидная (расширенная) матрица A:\n\n",A,"\n")  

F = A[:,4]
A = A[:,:4]

# обратное решение
X[n-1] = F[n-1]
for k in reversed(range(0, n-1, 1)):
  sum_row = 0
  for i in reversed(range(0, n, 1)):
    if (A[k][i] == 0.0):
      continue
    if (X[i] is not None):
      sum_row += A[k][i] * X[i]
  X[k] = F[k] - sum_row
print("\n\nX = ",X,"\n\n")

#вектор невязки
r = np.dot(A, X) - F
print("Вектор невязки: ",r,"\n\n")

#определитель
L = A_orig
L = np.column_stack((L, F))
print("L:\n\n",L,"\n")
for k in range(0, 4, 1):
  # вернём индекс максимального элемента по модулю из столбца
  index_max = np.argmax(abs(L[k:,k])) + k
  # print(A[index_max][k],"  ", abs(A[k:,k]))
  #меняем строки местами
  swap_row(L, k, index_max)
  # print(A,"\n") 
  # L[k] /= L[k][k]
  for i in range(k+1, n, 1):
      L[i] = L[i] - L[k] * L[i][k]
    
print("L:\n\n",L,"\n")  

void GetDeterminant(double **matrix, int size, double epsilon)
{
    //Предполагается, что матрица квадратная
    int pivot_index = -1;
    double pivot_value = 0;
    double determinant = 1;
    
    for(int i = 0; i < size; i++)
    {
        for(int j = i; j < size; j++)
        {
            if(abs(matrix[j][i]) > pivot_value)
            {
                pivot_index = j;
                pivot_value = abs(matrix[j][i]);
            }
        }
        
        //Если опорный элемент равен нулю (эпсилон для сброса погрешности)
        if(pivot_value < epsilon)
        {
            //Матрица вырождена
            return 0;
        }
        
        if(pivot_index != i)
        {
            //Обменяем строки местами
            SwapRows(matrix, pivot_index, i)
            determinant *= -1;
        }
        
        for(int j = i + 1; j < size; j++)
        {
            if(matrix[j][i] != 0)
            {
                multiplier = 1 / matrix[i][i] * matrix[j][i];
                
                for(int k = i; k < size; k++)
                {
                    matrix[j][k] -= matrix[i][k] * multiplier;
                }
            }
        }
        
        determinant *= matrix[i][i];
    }
    
    return determinant;
}