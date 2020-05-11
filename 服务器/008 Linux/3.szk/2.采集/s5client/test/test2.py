

import test1

# [
# 'PWD',
# 'USER',
# '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__',
# 'port']
# print(dir(test1))
#
# for  k in dir(test1):
#     if k.isupper():
#         print(k)
#         print(getattr(test1, k))

# test1.show()

# import importlib
# m = importlib.import_module('test1')
#
# m.show()

import traceback
def aaa():
    try:
        bb
    except Exception as e:
        print(traceback.format_exc())

aaa()
