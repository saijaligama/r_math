import random

class IntegerClass():
    def __init__(self):
        self.x = 0

    def integerRandomTests(self,data):
        num_of_questions = int(data['numOfQues'])
        f_num_digits = int(data['fnumDigits'])
        s_num_digits = int(data['sNumDigits'])
        operation = data['ASMD']

        result = {'questions': [], 'answers': []}
        for i in range(0, num_of_questions):
            first_num = random.randint(10 ** (f_num_digits - 1), 10 ** f_num_digits - 1)
            second_num = random.randint(10 ** (s_num_digits - 1), 10 ** s_num_digits - 1)

            if operation == '+':
                res = first_num + second_num
            elif operation == '-':
                res = first_num - second_num
            elif operation == '*':
                res = first_num * second_num
            elif operation == '/':
                if second_num == 0:
                    second_num = random.randint(10 ** (s_num_digits - 1), 10 ** s_num_digits - 1)
                    res = round(first_num // second_num, 2)
                else:
                    res = round(first_num // second_num, 2)
            else:
                return {'error': 'Invalid Operation'}

            question = str(first_num) + ' ' + operation + ' ' + str(second_num)
            result['questions'].append(question)
            res = round(res, 5)
            result['answers'].append(str(res))

        return result