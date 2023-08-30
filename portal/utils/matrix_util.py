def get_final_out_1(res):
    k = list(res)
    string = ''
    for z in k:
        for z2 in str(z).replace('[', '').replace(']', '').split():
            string += str(float(z2)) + ','
        string = string[:-1] + ';'
    return '{' + string[:-1] + '}'
