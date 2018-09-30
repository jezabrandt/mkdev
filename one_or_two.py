def one_or_two_dict(a):
    return {1: 2, 2: 1}[a]


print(one_or_two_dict(1))


def one_or_two_list(a):
    list_num = [1, 2]
    list_num.remove(a)
    return list_num[0]


print(one_or_two_list(2))


def one_or_two_set(a):
    set_of_num = {1, 2}
    set_a = set()
    set_a.add(a)
    res = (set_of_num ^ set_a)
    return [*res][0]


print(one_or_two_set(1))


def one_or_two_(a):
    return int(abs(-2 / a))


print(one_or_two_(1))
