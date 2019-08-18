#!/usr/bin/python
# -*- coding: utf-8 -*

def fun1():
    '''
    Python基础语法学习
    '''

    for item in ['a', 'b', 'c']:
        print item

    for item in ['a', 'b', 'c']:
        print item,

    print
    print "=========================================="

    squared = [x * 1 for x in range(4)]
    print squared

    print "=========================================="

    squared = [x ** 2 for x in range(4)]
    for item in squared:
        print item


def fun2():
    '''
    文件读取
    '''

    filename = raw_input("请输入文件名称:")
    fobj = open(filename, 'r')
    for eachLine in fobj:
        print eachLine,

    fobj.close();


def fun3():
    '''
    异常测试try-except
    '''

    try:
        filename = raw_input("请输入文件名称:")
        fobj = open(filename, 'r')
        for eachLine in fobj:
            print eachLine,

        fobj.close();
    except IOError, e:
        print '文件不存在', e


def fun4(debug = True):
    '''
    参数默认值
    '''

    if debug:
        print '函数参数默值为true'

    print "完成"

class FooClass(object):
    '''
    我使用Python定义的第一个类
    '''

    version = 0.1

    def __init__(self, name = "zhangsan"):
        '''
        类的构造方法
        '''

        self.name = name
        print '调用__init__方法完成'

    def showName(self):
        '''
        用户自定义方法
        '''

        print '属性name的值为', self.name
        print '类的名称为', self.__class__.__name__


if __name__ == '__main__':
    print fun1.__doc__
    # fun1()
    # fun2()
    # fun3()
    # fun4(False)
    fooClass = FooClass('lisi')
    fooClass.showName()