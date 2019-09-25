def sum_of_multiples(limit, multiples):
    ret_list = []
    list_of_products = []
    for i in multiples:
        if i == 0:
            continue
        j = 1
        while j < limit / i:
            if i * j < limit:
                list_of_products.append(i * j)
            j += 1
    [ret_list.append(x) for x in list_of_products if x not in ret_list]
    return sum(ret_list)
