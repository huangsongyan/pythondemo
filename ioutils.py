#encoding:utf-8

f = open('C:\HaxLogs.txt','r')

print f.read()

# f.close()


# with open('C:\HaxLogs.txt','r') as f:
#     print f.read()

for line in f.readlines():
    print(line.strip()) # 把末尾的'\n'删掉

#前面讲的默认都是读取文本文件，并且是ASCII编码的文本文件。要读取二进制文件，比如图片、视频等等，用'rb'模式打开文件即可：
# >>> f = open('/Users/michael/test.jpg', 'rb')
# >>> f.read()
# '\xff\xd8\xff\xe1\x00\x18Exif\x00\x00...' # 十六进制表示的字节

import codecs
with codecs.open('C:\HaxLogs.txt', 'r', 'gbk') as f:
    print f.read() # u'\u6d4b\u8bd5'

import os
print os.name
# print os.uname()

import json

d = dict(name='Bob',age=20, score=88)
print json.dumps(d)

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print json.loads(json_str)