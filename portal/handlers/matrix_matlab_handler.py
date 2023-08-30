from portal.application.matrix_operations import get_ones_zeros_eye, get_matrix, \
    get_transpose_inv_det, get_Diagonal_Trace_Size
from portal.utils.matrix_util import get_final_out_1


def matrix_matlab_calc(data):
    result_ = ''
    print(data['type'])
    if data['type'] == "Zeros" or data['type'] == "Ones":
        if str(data['matrix_matlab_Expression']).__contains__(','):
            temp_matrix_a = str(data['matrix_matlab_Expression']).replace('(', '').replace(')', '').split(',')
            final_ = []
            for num in temp_matrix_a:
                if num.isdigit() and int(num) == 0:
                    return {'result_': "Size cannot be zero.", 'status': "Failed"}
                elif num.isdigit():
                    final_.append(int(num))
                else:
                    return {'result_': "Size cannot be string.", 'status': "Failed"}
            result_ = get_ones_zeros_eye(tuple(final_), data['type'])
        else:
            return {'result_': "Please check entered expression", 'status': "Failed"}
    elif data['type'] == "Eyes":
        temp_matrix_a = str(data['matrix_matlab_Expression']).replace('(', '').replace(')', '').strip()
        if temp_matrix_a.isdigit() and int(temp_matrix_a) == 0:
            return {'result_': "Size cannot be zero.", 'status': "Failed"}
        elif temp_matrix_a.isdigit():
            temp_matrix_a = int(temp_matrix_a)
        else:
            return {'result_': "Size cannot be string.", 'status': "Failed"}
        result_ = get_ones_zeros_eye(temp_matrix_a, data['type'])
    elif data['type'] == "Det" or data['type'] == "Inverse" or data['type'] == "Transpose":
        if str(data['matrix_matlab_Expression']):
            temp_matrix_a = str(data['matrix_matlab_Expression']).replace('{', '').replace('}', '').split(';')
            matrix_a = get_matrix(temp_matrix_a)
            result_ = get_transpose_inv_det(matrix_a, data['type'])
            print("Inverse", result_)
            if data['type'] == "Det" and not isinstance(result_, str):
                return {'result_': float(result_), 'status': "Successful"}
        else:
            return {'result_': "Please check entered expression", 'status': "Failed"}
    elif data['type'] == "Diagonal" or data['type'] == "Size" or data['type'] == "Trace":
        if str(data['matrix_matlab_Expression']):
            temp_matrix_a = str(data['matrix_matlab_Expression']).replace('{', '').replace('}', '').split(';')
            print("size of matrix:", temp_matrix_a)
            matrix_a = get_matrix(temp_matrix_a)
            result_ = get_Diagonal_Trace_Size(matrix_a, data['type'])
            print("Result", result_)
            if data['type'] == "Size" and not isinstance(result_, str):
                return {'result_': tuple(result_), 'status': "Successful"}
            elif data['type'] == "Trace" and not isinstance(result_, str):
                return {'result_': float(result_), 'status': "Successful"}
            elif data['type'] == 'Diagonal' and not isinstance(result_, str):
                return {'result_': get_final_out_1(result_), 'status': "Successful"}
            else:
                return {'result_': "Please check matrix expression", 'status': "Failed"}
    else:
        return {'result_': "Operation not understood", 'status': "Failed"}

    if isinstance(result_, str):
        if result_ == 'The matrix is singular':
            return {'result_': "The matrix is singular", 'status': "Failed"}
        elif result_ == 'The matrix is not square':
            return {'result_': "The matrix is not square", 'status': "Failed"}
        elif result_ == 'Please check matrix expression':
            return {'result_': "Please check matrix expression", 'status': "Failed"}

    if data['type'] == "Zeros" or data['type'] == "Ones" or data['type'] == "Eyes":
        str_final_ = get_final_out_1(result_)
    else:
        str_final_ = get_final_out_1(result_)
    if str_final_:
        str_final_ = str_final_
        return {'result_': str_final_, 'status': "Successful"}
    else:
        return {'result_': "Please check entered expression", 'status': "Failed"}
