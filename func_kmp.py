def cal(needle='aababaaba'):
    dict_step = dict()
    for index, letter in enumerate(needle):
        dict_step.setdefault(index, 0)
        for i in range(min(index, len(needle) - index)):
            if needle[:i+1] == needle[index:index+i+1] and i + 1 > dict_step[index]: 
                dict_step[index] = i
    return dict_step


def match(target, pattern):
    dict_pattern = cal(pattern)
    start = 0
    target_index = -1
    index = -1
    index_tmp = 0
    while True:
        if index_tmp >= len(pattern):
            index = start - len(pattern)
            break
        if start >= len(target):
            break
        if pattern[index_tmp] == target[start]:
            index_tmp += 1
            start += 1
        else:
            start += dict_pattern[index_tmp] + 1
            index_tmp = dict_pattern[index_tmp] 
    print(index)
        
if __name__ == '__main__':
    match('abacaabacabacabaabb', 'abacab')
