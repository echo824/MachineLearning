# # 变量定义
# x = 10           # 整数
# y = 3.14         # 浮点数
# name = "Alice"   # 字符串
# is_active = True # 布尔值
#
# # 多变量赋值
# a, b, c = 1, 2, "three"
#
# # 查看数据类型
# print(type(x))         # <class 'int'>
# print(type(y))         # <class 'float'>
# print(type(name))      # <class 'str'>
# print(type(is_active)) # <class 'bool'>
#
# del a
# a = 111
# print(isinstance(a, int))

#!/usr/bin/python3

# my_str = 'Runoob'       # 定义一个字符串变量（避免使用 str 作为变量名，会覆盖内置类型）
#
# print(my_str)           # 打印整个字符串：Runoob
# print(my_str[0:-1])     # 打印索引 0 到倒数第二个字符（不含最后一个）：Runoo
# print(my_str[0])        # 打印第一个字符：R
# print(my_str[2:5])      # 打印索引 2、3、4 的字符（不含索引 5）：noo
# print(my_str[2:])       # 打印从索引 2 开始到末尾：noob
# print(my_str * 2)       # 重复打印两次：RunoobRunoob
# print(my_str + "TEST")  # 字符串拼接：RunoobTEST



# def reverse_words(input):
#
#     # 通过空格将字符串分隔，把各个单词分隔为列表
#     inputWords = input.split(" ")
#
#     # inputWords[-1::-1] 三个参数说明：
#     # 第一个参数 -1 表示从最后一个元素开始
#     # 第二个参数为空，表示移动到列表开头
#     # 第三个参数 -1 表示逆向步进（每次向左移动一个位置）
#     inputWords = inputWords[-1::-1]
#
#     # 重新用空格拼接单词
#     output = ' '.join(inputWords)
#
#     return output
#
# if __name__ == "__main__":
#     input = 'I like runoob'
#     rw = reverse_words(input)
#     print(rw)

sites = {'Google', 'Taobao', 'Runoob', 'Facebook', 'Zhihu', 'Baidu'}

print(sites)   # 输出集合（无序，重复元素会被自动去掉）

# 成员测试
if 'Runoob' in sites:
    print('Runoob 在集合中')
else:
    print('Runoob 不在集合中')

# set 可以进行集合运算
a = set('abracadabra')
b = set('alacazam')

print(a)           # a 中的唯一字符

print(a - b)       # a 和 b 的差集（在 a 中但不在 b 中）
print(a | b)       # a 和 b 的并集（在 a 或 b 中）
print(a & b)       # a 和 b 的交集（同时在 a 和 b 中）
print(a ^ b)       # a 和 b 的对称差集（在 a 或 b 中，但不同时存在）
