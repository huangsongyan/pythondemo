#encoding:utf-8
import math

#条件判断
a = 100
if a>=0:
    print a
else:
    print -a

#转义字符 \
print 'I\'m ok'

#转义字符\可以转义很多字符，比如\n表示换行，\t表示制表符，字符\本身也要转义，所以\\表示的字符就是\，可以在Python的交互式命令行用print打印字符串看看：

#Python还允许用r''表示''内部的字符串默认不转义
print r'\\t\\t'

#多行输出

#三个表示多行输出
print '''line1
line2
line3'''

print True

print 3>2

#布尔值可以用and、or和not运算。

#and运算是与运算，只有所有都为True，and运算结果才是True：
print True and False

#or运算是或运算，只要其中有一个为True，or运算结果就是True：
print True or False

#not运算是非运算，它是一个单目运算符，把True变成False，False变成True：

print not True


#空值是Python里一个特殊的值，用None表示

#所谓常量就是不能变的变量，比如常用的数学常数π就是一个常量。在Python中，通常用全部大写的变量名表示常量：

print math.pi



