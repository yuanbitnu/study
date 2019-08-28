# Python中的字典是一种映射类型,映射属于可变对象,目前标准的映射类型只有dict(字典)一种
# 字典的键必须是非可变对象
import sys


def main():
        # 创建空字典
    dic = {}
    print(type(dic))  # result = <class 'dict'>
    print(dic)  # result = {}

    dic = dict()
    print(type(dic))  # result = <class 'dict'>
    print(dic)  # result = {}

    # 创建非空字典
    # 使用{}创建
    dic = {'one': 1, 'two': 2, 'three': 3}  # 键是非可变对象
    print(dic)
    # 使用dict(),传入关键字参数,则会创建一个形参为键,实参为值的字典
    dic = dict(one=1)
    print(dic)  # result = {'one': 1}
    # 使用dict(),传入每一项都为包含两个元素的可迭代对象
    result = zip(['one', 'two', 'three'], (1, 2, 3))
    # result = (('one', 1), ('two', 2), ('three', 3))  每一项都包含两个元素的可迭代对象
    print(tuple(result))
    # print(list(result)) #result = [('one', 1), ('two', 2), ('three', 3)]   每一项都包含两个元素的可迭代对象

    result = zip(['one', 'two', 'three'], (1, 2, 3))
    dic = dict(result)
    print(dic)

    # 使用dict(),传入一个字典
    result = dict({'one': 1, 'three': 3, 'two': 2})
    print(result)

    # 获取字典中的值
    # 使用[]获取,key存在则返回对应值,不存在则抛出 KeyError: '冷面' 异常
    dic = {'元芳': 78, '狄仁杰': 82, '武则天': 60}
    print('使用[]获取值:', dic['元芳'])
    # print(dic['冷面']) #result = KeyError: '冷面'

    # 使用dict.get()方法获取,key存在则返回对应的值,不存在则返回default值,如果未设置default则返回None
    # 使用dict.get()方法设置的default值不会影响原字典
    # 使用dict.get()方法获取不会引发 KeyError 异常
    dic = {'元芳': 78, '狄仁杰': 82, '武则天': 60}
    print('使用dict.get()获取值:', dic.get('元芳'))
    print('使用dict.get()获取值/默认值', dic.get('冷面', 98))
    print(dic)

    # 对字典进行遍历,遍历的其实是键,通过键再取对应的值
    dic = {'元芳': 78, '狄仁杰': 82, '武则天': 60}
    for elem in dic:
        print(f'键是:{elem}; 值是{dic[elem]}')

    # 更新字典中的元素
        # 使用[]更新单个元素,覆盖之前的
    dic = {'元芳': 78, '狄仁杰': 82, '武则天': 60}
    print('使用[]更新前 = ', dic)
    dic['元芳'] = 90  # 如果字典中存在该键则覆盖旧值
    dic['冷面'] = 102  # 如果字典中不存在该键,则添加
    print('使用[]更新后 = ', dic)

    # 使用dict.update()更新多个元素,参数和dict()函数创建字典使用的参数一致,并且如果有相同的元素则覆盖之前的
    dic = {'元芳': 78, '狄仁杰': 82, '武则天': 60}
    dic_update = [('方齐禾', 20), ('诸葛驭狼', 30), ('狄仁杰', 100)]  # 覆盖dic中的'狄仁杰':82
    print('使用update()更新前 = ', dic)
    dic.update(dic_update)
    dic.update(冷面=67, 方启鹤=85)
    print('使用update()更新后 = ', dic)

    # 删除字典中的元素
    # 使用dict.popitem()删除,按照LIFO(后进先出)的顺序删除元素,并返回删除的元素,如果字典为空则引发KeyError异常
    dic = {'元芳': 78, '狄仁杰': 82, '武则天': 60}
    print('使用dict.popitem()删除元素前: ', dic)
    popitem = dic.popitem()
    print('使用dict.popitem()删除后返回的值: ', popitem)
    print('使用dict.popitem()删除元素后: ', dic)
    dic.popitem()
    dic.popitem()  # 此时dic中元素已删完
    # dic.popitem() #对一个空dic执行popitme会引发 KeyError: 'popitem(): dictionary is empty' 异常

    # 使用dict.pop(key,[default])方法删除指定元素,如果字典存在该Key则返回其值,否则返回default,
    # 如果Key不存在且default未给出,则引发KeyError异常
    dic = {'元芳': 78, '狄仁杰': 82, '武则天': 60}
    print('使用dict.pop(key,[default])删除元素前: ', dic)
    popvalue = dic.pop('元芳')
    print('使用dict.pop()删除后返回的值: ', popvalue)
    print('使用dict.pop(key,[default])删除元素后: ', dic)
    popvalue = dic.pop('冷面', '默认值')
    print('使用dict.pop(key,[default])删除一个不存在的key,且指定了默认值时的返回值: ', popvalue)
    # popvalue = dic.pop('冷面') #未指定默认值引发KeyError异常


if __name__ == '__main__':
    main()
