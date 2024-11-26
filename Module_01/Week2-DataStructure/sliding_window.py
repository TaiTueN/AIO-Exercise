def max_kernel(num_list, k):
    res = []
    for i in range(len(num_list)-k+1):
        res.append(max(num_list[i: i+k]))
    return res


num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
k = 3
print(max_kernel(num_list, k))
