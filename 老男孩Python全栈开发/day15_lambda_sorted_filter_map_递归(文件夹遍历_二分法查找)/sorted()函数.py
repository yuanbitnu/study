# sorted()函数用于可迭代对象进行排序,参数key是一个函数，将可迭代对象中的每一个元素传入该函数，并将返回的值作为排序的权重，返回排序后的新列表（不会改变原有列表）
lis = [1, 3, 18, 3, 78, 1]
lis_new = sorted(lis)
print(lis_new)


def fn(s):
    return len(s)


lis = ['adasd', 'as', 'jgfjgj', '张三', '王儿吧']
lis_new = sorted(lis, key=fn)
print(lis_new)

lis = [{'mm': 222}, {'mm': 333}, {'mm': 111}]
lis_new = sorted(lis, key=lambda item: item['mm'])
print(list(lis_new))
