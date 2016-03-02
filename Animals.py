#encoding:utf-8

class Animsla(object):
    def run(self):
        print 'run'


#使用type()

import types

print type(123)==type(456)

print types('abc')==types.StringType

# >>> import types
# >>> type('abc')==types.StringType
# True
# >>> type(u'abc')==types.UnicodeType
# True
# >>> type([])==types.ListType
# True
# >>> type(str)==types.TypeType
# True

#最后注意到有一种类型就叫TypeType，所有类型本身的类型就是TypeType，比如：
print (int)==type(str)==types.TypeType

#并且还可以判断一个变量是否是某些类型中的一种，比如下面的代码就可以判断是否是str或者unicode：
isinstance('a', (str, unicode))

#使用dir()

#如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法：

#剩下的都是普通属性或方法，比如lower()返回小写的字符串：

print 'ABC'.lower()

#仅仅把属性和方法列出来是不够的，配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态：

#__slots__ = ('name', 'age')

