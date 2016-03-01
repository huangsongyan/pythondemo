#encoding:utf-8
#字典

d = {'name':'hsy','age':18}

print d

print d['name']

#二是通过dict提供的get方法，如果key不存在，可以返回None，或者自己指定的value：
print d.get("name")

print d.get("height",-1)
print d.get("height")

#要避免key不存在的错误，有两种办法，一是通过in判断key是否存在：

print "height" in d