#!/usr/bin/python
# -*- coding: utf-8 -*

# 无论是直接执行当前的模块，还是此模块别其他的模块导入，这个输出均会直接执行
print "全局输出"

class Module1:
    '''
    测试被导入的模块是否会自动执行__init___方法
    '''

    def __init__(self):
        '''
        虽然当模块被导入时类会定义，但是被导入的模块中的类的定义中的__init__方法不会自动执行；除非在导入的模块中创建了被导入模块中的某个类的对象后，被导入模块中
        该类的__init__方法才会被执行
        '''

        print "被导入的模块自动执行__init__方法"


def fun1():
    '''

    '''

    print "MyModule中的fun1执行"

if __name__ == 'main':
    print '执行MyModule模块的main'