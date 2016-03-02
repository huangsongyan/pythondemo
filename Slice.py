#encoding:utf-8
#切片

L=['1','2','3']

print L[-1]

print L[-2:]

print L[-2:-1]

#取前N个元素
# L[:n]
#取倒数N个元素
# L[-n:]

L = range(100)
#前10个数，每两个取一个
L[:10:2]

#甚至什么都不写，只写[:]就可以原样复制一个list：
L[:]


#判断是否可以迭代
#isinstance('abc', Iterable)

#迭代

#dict
d={'a':1,'b':2,'c':3}
#只打印key
for key in d:
    print key

#打印值
for value in d.itervalues():
    print value



#打印键值

for k,v in d.iteritems():
    print k,v

#判断是否是字符串
#isinstance(x, str)

#斐波拉契数列
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
