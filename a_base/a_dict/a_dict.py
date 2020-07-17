# 1-Counter
# Counter是一个dict子类，主要是用来对你访问的对象的频率进行计数。
# 常用方法：
#
# elements()：返回一个迭代器，每个元素重复计算的个数，如果一个元素的计数小于1,就会被忽略。
# most_common([n])：返回一个列表，提供n个访问频率最高的元素和计数
# subtract([iterable-or-mapping])：从迭代对象中减去元素，输入输出可以是0或者负数
# update([iterable-or-mapping])：从迭代对象计数元素或者从另一个 映射对象 (或计数器) 添加。

from collections import Counter

# 统计字符出现的次数
count_el = Counter('hello world')
# Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})

# 统计单词数
count_word1 = Counter('hello world hello world hello nihao'.split())
# Counter({'hello': 3, 'world': 2, 'nihao': 1})

# 元素获取
list(count_word1.elements())
# ['hello', 'hello', 'hello', 'world', 'world', 'nihao']

count_word2 = Counter('hello hehe'.split())
# Counter({'hello': 1})
# 求和
print(count_word1 + count_word2)
# Counter({'hello': 4, 'world': 2, 'nihao': 1})

# 求差
print(count_word1 - count_word2)
# Counter({'hello': 2, 'world': 2, 'nihao': 1})

# 清空
count_word1.clear()
print(count_word1)
Counter()

# 2-namedtuple
# 三种定义命名元组的方法：第一个参数是命名元组的构造器（如下的：Person，Human）
from collections import namedtuple

Person = namedtuple('Person', ['age', 'height', 'name'])
xqq = Person(30, 178, 'xqq')
tom = Person(*(30, 178, 'Tom'))
print(tom)
