#!/usr/bin/python
# -*- coding: utf-8 -*

import MyModule
# from MyModule import Module1

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

    # 普通成员变量
    version = 0.1
    # 单个下划线开始的为私有成员变量
    __version = 0.2
    # 以双下划线开始和结束的属性和方法为Python中已经预先定义的系统属性和方法，
    # 都有特殊的含义，用户在定义时最好不要这样定义
    # 例如__init__

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

class SubClass(FooClass):
    '''
    定义一个子类，继承父类FooClass
    '''


def fun5():
    '''
    赋值
    '''

    # 连续赋值
    x = y = z = 1
    print "x = %d, y = %d, z = %d" % (x, y, z)

    # 多元赋值
    x, y, z = 'a', 'b', 'c' # 标准方式应该加上小括号，说明是对一个元组进行赋值
    print "x = %s, y = %s, z = %s" %(x, y, z)

    # 变量值交换
    (a, b) = 1, 2
    print "a = %d, b = %d" %(a, b)
    (a, b) = (b, a)
    print "a = %d, b = %d" %(a, b)

    # 约定
    # _XXX_    系统定义名字
    # _XXX    类中定义的私有成员变量



if __name__ == '__main__':
    # print fun1.__doc__
    # fun1()
    # fun2()
    # fun3()
    # fun4(False)
    fooClass = FooClass('lisi')
    fooClass.showName()
    fooClass.version

    subClass = SubClass(fooClass)

    fun5()

    module1 = MyModule.Module1()
    MyModule.fun1()
