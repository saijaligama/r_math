import numpy as np
import mpmath as mp


def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

def get_matrix(temp_matrix_a):
    matrix_ = []
    print(temp_matrix_a)
    for string in temp_matrix_a:
        let_=string.split(',')
        if len(let_)>1:
            nums = []
            print('smdn')
            for num in string.split(','):
                if is_float(num):
                    nums.append(float(num))
                else:
                    nums.append(num)  # append the string as is
            matrix_.append(nums)
        else:
            if string.isdigit():
                matrix_.append(int(string))
            else:
                matrix_.append(string)

        print('matrix_',matrix_)
    return matrix_


def is_valid(matrix):
    for row in matrix:
        if isinstance(row, list):
            for element in row:
                if not isinstance(element, int):
                    if not isinstance(element, float):
                        return False
        else:
            if not isinstance(row, int):
                if not isinstance(row, float):
                    return False
    return True


def matrix_arithmetic(A, B):
    check_valid_a = A
    check_valid_B = B
    try:
        A = np.array(A)
    except ValueError:
        return {'OutPut': 'Please check matrice 1'}
    try:
        B = np.array(B)
    except ValueError:
        return {'OutPut': 'Please check matrice 2'}
    # if A.shape != B.shape:
    #     return {'OutPut': 'The input matrices have different shapes'}
    if not is_valid(check_valid_a):
        return {'OutPut': 'Please check matrix 1'}
    if not is_valid(check_valid_B):
        return {'OutPut': 'Please check matrix 2'}
    return {'OutPut': 'Successful'}


def matrix_arithmetic_operations(A, B, operation):
    A = np.matrix(A)
    B = np.matrix(B)
    if operation == '+':
        try:
            if A.shape==B.shape:
                C = A+B
            else:
                return f'Error: dimension mismatch'
        except ValueError as e:
            return f'Error: ({e})'
        except Exception as e:
            return f'Error: ({e})'
    elif operation == '-':
        try:
            C = A- B
        except ValueError as e:
            return f'Error: ({e})'
        except Exception as e:
            return f'Error: ({e})'
    elif operation == '*':
        try:
            C = np.matmul(A, B)
        except ValueError as e:
            return f'Error: ({e})'
        except Exception as e:
            return f'Error: ({e})'
    elif operation == '/':
        try:
            C = np.matmul(A,np.linalg.inv(B))
        except Exception as e:
             return f'Error: ({e})'
    else:
        return None
    return C


def get_ones_zeros_eye(matrix, type):
    if type == 'Zeros':
        matrix = np.zeros(matrix)
    elif type == 'Ones':
        matrix = np.ones(matrix)
    elif type == 'Eyes':
        matrix = np.eye(matrix)
    return matrix


def is_square(matrix):
    return matrix.shape[0] == matrix.shape[1]

#
# det_A = np.linalg.det(A)
#
# if det_A == 0:
#     print("Matrix A is not invertible")
# else:
#     A_inv = np.linalg.inv(A)
#     print("Inverse of A:")
#     print(A_inv)


def get_inverse(matrix):
    try:
        matrix_final = np.array(matrix)
        if is_square(matrix_final):
            det_A = np.linalg.det(matrix_final)
            if det_A == 0:
                return "Matrix B is not invertible"
            else:
                inv_matrix = np.linalg.inv(matrix_final)
        else:
            inv_matrix = np.linalg.pinv(matrix_final)
            inv_matrix=inv_matrix.tolist()
        return inv_matrix
    except ValueError:
        return 'Please check matrix expression'
    except Exception as e:
        return f'Error: Please check matrix expression ({e})'


def get_transpose_inv_det(matrix, type):
    mp.dps = 5
    check_valid_a = matrix
    try:
        matrix = np.matrix(matrix, dtype=float)
        matrix_final = np.array(matrix)
    except ValueError:
        return 'Please check matrix expression'
    if not is_valid(check_valid_a):
        return 'Please check matrix expression'
    print("Shape",matrix.shape, matrix )
    if type=='Transpose':
        transpose_matrix = matrix.transpose()
        return transpose_matrix
    if matrix.shape[0] == matrix.shape[1]:
        det = np.linalg.det(matrix)
        if type=='Det':
            return det
        
        if type=='Inverse':
            if det != 0:
                inv_matrix = np.linalg.inv(matrix)
                return inv_matrix
            else:
                return "The matrix is singular"
    else:
        return "The matrix is not square"


def get_Diagonal_Trace_Size(matrix, type):
    check_valid_a = matrix
    try:
        matrix = np.matrix(matrix, dtype=float)
    except ValueError:
        return 'Please check matrix expression'
    if not is_valid(check_valid_a):
        return 'Please check matrix expression'
    if type=='Diagonal':
        diagonal = matrix.diagonal()
        return diagonal
    elif type == 'Size':
        size = matrix.shape
        return size
    else:
        trace = matrix.trace()
        return trace


