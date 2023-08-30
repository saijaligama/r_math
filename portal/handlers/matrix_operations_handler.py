import re
from portal.utils.matrix_util import get_final_out_1
from portal.application.matrix_operations import matrix_arithmetic, matrix_arithmetic_operations, get_matrix


def matrix_calc(data):
    match = re.search(r"(?<=})(.*?)(?={)", data['matrix_expression_1_input'])
    if isinstance(match, type(None)):
        return {'error_msg': "Syntax error", 'status': "Failed", 'result_': '-----'}
    operation_ = match.group(1).strip()
    if len(operation_) != 1:
        return {'result_': '-----', 'status': "Failed", 'error_msg': "Syntax error"}
    print(match, data['matrix_expression_1_input'])
    ixx = match.group(1).index(operation_)
    ix = match.span()
    tmp_a = data['matrix_expression_1_input'][:ix[0] + ixx]
    tmp_b = data['matrix_expression_1_input'][ix[1] - ixx:]
    if tmp_a.count("{") != tmp_a.count("}") or tmp_a.count("{") == 0 or tmp_a.count("}") == 0:
        return {'result_': '-----', 'status': "Failed", 'error_msg': "Syntax error"}
    if tmp_b.count("{") != tmp_b.count("}") or tmp_b.count("{") == 0 or tmp_b.count("}") == 0:
        return {'error_msg': "Syntax error", 'status': "Failed", 'result_': '-----'}
    temp_matrix_a = tmp_a.replace('{', '').replace('}', '').strip().split(';')
    temp_matrix_b = tmp_b.replace('{', '').replace('}', '').strip().split(';')

    print('matrix_expression_1_input', temp_matrix_a)
    print('matrix_expression_2_input', temp_matrix_b)
    print('Matrix_Action', operation_)
    # exit()
    matrix_a = get_matrix(temp_matrix_a)
    matrix_b = get_matrix(temp_matrix_b)
    print('matrix_a', matrix_a)
    print('matrix_b', matrix_b)

    check_list_ = matrix_arithmetic(matrix_a, matrix_b)
    print('check_list_', check_list_)
    if check_list_['OutPut'] == 'Successful':
        result_ = matrix_arithmetic_operations(matrix_a, matrix_b, operation_)
        print("Result", result_, type(result_))
        if isinstance(result_, type(None)):
            return {'result_': '-----', 'status': "Failed", 'error_msg': "Syntax Error"}

        if isinstance(result_, str):
            return {'result_': '-----', 'status': "Failed", 'error_msg': result_}

        str_final_ = get_final_out_1(result_)
        # str_final_ = str_final_ + '}'
        return {'result_': str_final_, 'status': str(check_list_['OutPut']), 'error_msg': '-----'}
    else:
        return {'result_': '-----', 'status': str(check_list_['OutPut']), 'error_msg': str(result_)}
