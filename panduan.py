#encoding:utf-8
#条件判断

age = 3
if age >=18:
    print 'your age is',age
    print 'adult'
else:
    print 'your age is',age
    print 'teenager'

#循环

names = [1,2,3,4]

for name in names:
    print name

# 1加到10的数
num = [1,2,3,4,5,6,7,8,9,10]
sum = 0
for x in num:
    sum += x
print sum

#生成一个整数序列
print range(5)
#[0, 1, 2, 3, 4]
