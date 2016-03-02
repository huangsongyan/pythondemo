#encoding:utf-8

# Pillow is a maintained fork of PIL, so I recommend using Pillow. But you can't have both installed at the same time.
#
# First, remove both PIL and Pillow.
#
# Then install Pillow with pip install pillow (although, depending on platform, you may need some prerequisites).
#
# Then make sure code is using from PIL import Image rather than import Image.


from PIL import Image

import sys

print sys.path

#模块搜索路径

#默认情况下，Python解释器会搜索当前目录、所有已安装的内置模块和第三方模块，搜索路径存放在sys模块的path变量中：

#一是直接修改sys.path，添加要搜索的目录：
#第二种方法是设置环境变量PYTHONPATH，该环境变量的内容会被自动添加到模块搜索路径中。设置方式与设置Path环境变量类似。注意只需要添加你自己的搜索路径，Python自己本身的搜索路径不受影响。

#使用__future__