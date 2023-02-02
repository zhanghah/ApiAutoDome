'''
Author: 张前薄
Date: 2023-02-02 09:48:33
email: 1915579714@qq.com
FilePath: \ApiAutoDome\test.py
'''
import os.path
import os

dir = os.walk(os.path.abspath(os.path.join(os.path.dirname(__file__))))
for root, dirs, files in dir:
    print('root', root)
    print('dirs', dirs)
    print('files', files)