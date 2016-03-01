#encoding:utf-8

#自定义函数
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x

print my_abs(10)

#空函数
def nop():
    pass

age = 30
if age >=18:
    pass

def my_abs2(x):
    if not isinstance(x,(int,float)):
        raise TypeError('bad operand type')
    if x >=0:
        return x
    else:
        return -x

#返回多个值
import math
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

x,y = move(100,100,60,math.pi/6)

print x,y

#在语法上，返回一个tuple可以省略括号，而多个变量可以同时接收一个tuple，按位置赋给对应的值，
r = move(100,100,60,math.pi/6)
print  r

#默认参数
def enroll(name, gender, age=6, city='Beijing'):
    print 'name:', name
    print 'gender:', gender
    print 'age:', age
    print 'city:', city

enroll('hsy','F',age=10)
enroll('hsy','F',city='zhuhai')

#注意事项

#定义一个函数，传入一个list，添加一个END再返回：
def add_end(L=[]):
    L.append('END')
    return L

def add_end2(L=None):
    if L is None:
        L = []
    L.append('END')
    return L

#可变参数

def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

nums = [1,2,3]
calc(nums[0],nums[1],nums[2])
print 'sum is',calc(*nums)