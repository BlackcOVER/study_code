def merge_sort(data_list):
    # 归并排序
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
    # 冒泡排序
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
    # 快排
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


def heapify(list_, n, index):
    # 堆排序递归子函数
    leatest = index
    left = index * 2 + 1
    right = index * 2 + 2
    if left < n and list_[leatest] < list_[left]:
        leatest = left
    if right < n and list_[leatest] < list_[right]:
        leatest = right
    if leatest != index:
        tmp = list_[leatest]
        list_[leatest] = list_[index]
        list_[index] = tmp
        heapify(list_, n, leatest)


def heapsort(list_):
    # 堆排序
    index = len(list_) // 2 - 1
    n = len(list_)
    for i in range(index, -1, -1):
        heapify(list_, n, i)
    for i in range(n - 1, -1, -1):
        tmp = list_[0] 
        list_[0] = list_[i]
        list_[i] = tmp
        heapify(list_, i, 0)
    print(list_)


if __name__ == '__main__':
    data = [1, 2, 8, 5, 123, 7, 3, 4]
    result = merge_sort(data)
    print(result)
