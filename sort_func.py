def merge_sort(data_list):
    if len(data_list) <= 1:
        return data_list
    mid_index =  len(data_list) // 2
    left_data = merge_sort(data_list[:mid_index])
    right_data = merge_sort(data_list[mid_index:])
    result = []
    while left_data and right_data:
        if left_data[0] < right_data[0]:
            result.append(left_data[0])
            left_data.pop(0)
        else:
            result.append(right_data[0])
            right_data.pop(0)
    if left_data:
        result.extend(left_data)
    elif right_data:
        result.extend(right_data)
    return result

            
def bubble_sort(data_list, begin):
    if begin >= len(data_list) - 1:
        return
    min_index = len(data_list) - 1
    for i in range(len(data_list)-1, begin - 1 ,-1):
        if data_list[i] <= data_list[min_index]:
            min_index = i
    temp = data_list[min_index]
    data_list[min_index] = data_list[begin]
    data_list[begin] = temp
    bubble_sort(data_list, begin + 1)


def quick_sort(data_list, left, right):
    if left >= right:
        return
    i = left
    j = right
    origin = data_list[left]
    while i < j:
        while i < j and data_list[j] > origin:
            j -= 1
        data_list[i] = data_list[j]
        while i < j and data_list[i] < origin:
            i += 1
        data_list[j] = data_list[i]
    data_list[i] = origin
    quick_sort(data_list, left, i - 1)
    quick_sort(data_list, i + 1, right)

if __name__ == '__main__':
    data = [1, 2, 8, 5, 123, 7, 3, 4]
    result = merge_sort(data)
    print(result)
