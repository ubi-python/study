# question 9

import math

pow_num_list = list()
idx = 1
flag = False
while (flag != True):
    c_powed = math.pow(idx, 2)
    idx += 1
    if len(pow_num_list) < 3:
        pow_num_list.append(c_powed)
        continue
    # b_powed = pow_num_list[-1]
    for b_powed in pow_num_list:
        a_powed = c_powed - b_powed

        if a_powed in pow_num_list:
            print(c_powed, '-', b_powed, '=', a_powed)
            a = math.sqrt(a_powed)
            b = math.sqrt(b_powed)
            c = math.sqrt(c_powed)
            if 1000 == (a + b + c):
                print(a * b * c)
                flag = True
                break
            elif 1000 < (a + b + c):
                print('Not Found')
                break
    pow_num_list.append(c_powed)
