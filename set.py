#encoding:utf-8

#set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。

#要创建一个set，需要提供一个list作为输入集合：
a = set([1,2,3,4,5,5])

a.add(6)

print a

a.remove(5)

print a