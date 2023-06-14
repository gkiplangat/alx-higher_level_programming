def weight_average(my_list=[]):
    if not my_list:
        return 0

    sum_score = 0
    sum_weight = 0
    for item in my_list:
        sum_score += item[0] * item[1]
        sum_weight += item[1]

    return sum_score / sum_weight

