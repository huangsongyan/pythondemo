#encoding:utf-8

#list 集合 list。list是一种有序的集合，可以随时添加和删除其中的元素。
classmates = ['hsy','longlomg','chouyu','jinhao']

print classmates

print len(classmates)

print classmates[0]

#取最后一个元素
print classmates[-1]

#插入元素
classmates.insert(1,'haha')

print classmates

#要删除list末尾的元素，用pop()方法：
classmates.pop()

#要删除指定位置的元素，用pop(i)方法，其中i是索引位置：
classmates.pop(1)

print classmates

#要把某个元素替换成别的元素，可以直接赋值给对应的索引位置：
classmates[1] = 'hh'

#集合里面可以有不同的类型

L=['hello',19,True]

print L

