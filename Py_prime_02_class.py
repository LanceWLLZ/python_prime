# _*_ coding: utf-8 _*_
# 开发人员：Lance_wllz
# 开发人员 86186
# 开发时间 2019/8/270:01
# 文件名称 Py_prime_02_class
# 开发工具:PyCharm

# 类以及相关内容介绍
''''''
'''
为什么要面向对象编程
    面向对象的编程带来的主要好处之一是代码的重用，实现这种重用的方法之一是通过继承机制。
    通过继承创建的新类称为子类或派生类，被继承的类称为基类、父类或超类。
    继承语法
相关概念
    类(Class): 用来描述具有相同的属性和方法的对象的集合。它定义了该集合中每个对象所共有的属性和方法。对象是类的实例。
    类变量：类变量在整个实例化的对象中是公用的。类变量定义在类中且在函数体之外。类变量通常不作为实例变量使用。
    数据成员：类变量或者实例变量, 用于处理类及其实例对象的相关的数据。
    方法重写：如果从父类继承的方法不能满足子类的需求，可以对其进行改写，这个过程叫方法的覆盖（override），也称为方法的重写。
    局部变量：定义在方法中的变量，只作用于当前实例的类。
    实例变量：在类的声明中，属性是用变量来表示的。这种变量就称为实例变量，是在类声明的内部但是在类的其他成员方法之外声明的。
    继承：即一个派生类（derived class）继承基类（base class）的字段和方法。继承也允许把一个派生类的对象作为一个基类对象对待。
          例如，有这样一个设计：一个Dog类型的对象派生自Animal类，这是模拟"是一个（is-a）"关系（例图，Dog是一个Animal）。
    实例化：创建一个类的实例，类的具体对象。
    方法：类中定义的函数。在类的内部，使用 def 关键字可以为类定义一个方法，
          与一般函数定义不同，类方法必须包含参数 self,且为第一个参数
    对象：通过类定义的数据结构实例。对象包括两个数据成员（类变量和实例变量）和方法。
区分类变量和实例变量
    类变量存在类的内存里，实例变量存在于某个实例中
    如果同时有类变量和实例变量，程序执行时，首先去找实例变量，如果实例变量不存在，就去执行类变量
    变量可以在程序里增加删除

简单理解类和实例的关系
    果我们把类比作一个建筑图纸（一张房子的蓝图），那么对象就是根据这个图纸建的实实在在的房子。而self则是这个房子对应的门牌，
    这些房子可能住着不同的人，他们需要这些门牌找到对应的家。
    类中的属性和对象就像给这个房子设置的各种设施，一套房子建好，当然就拥有这些设施，
    当然你也可以根据自己的需求要不要这些设施，或者改装一下。

'''
x = 2
#   python 01   类变量和实例变量 类的私有属性
'''
    __private_attrs：两个下划线开头，声明该属性为私有，不能在类的外部被使用或直接访问。
        在类内部的方法中使用时 self.__private_attrs。
    Python不允许实例化的类访问私有数据，
        但你可以使用 object._className__attrName（ 对象名._类名__私有属性名 ）访问属性
    _foo: 以单下划线开头的表示的是 protected 类型的变量，
        即保护类型只能允许其本身与子类进行访问，不能用于 from module import *
'''
if (x == 1):
    class Role:
        n = '123'
        name = 'lei'
        __private_station = '深蹲局'
        _location = 'chengdu'

        def __init__(self, name, role, weapon):
            self.name = name
            self.role = role
            self.weapon = weapon

        def shot(self):
            print('is shotting')

        def secret(self):
            print(self.name,'是',self.__private_station,'的人了')

    # print(Role.__private_station) # 出错，程序中不能调用
    r1 = Role('xiaoming', 'police', 'AK47')
    r1.secret()
    # print(r1.__private_station)# 报错，实例不能直接访问私有
    print(r1._Role__private_station)# 可以用加下划线的方式在程序中引访问
    print(Role._location) # 保护变量类，子类，实例都可以引用
    r1._location = 'beijing'
    print(r1._location)
    print(Role.n, Role.name)
    # Role.shot() # 报错，没有实例化没有self
    print(r1.n, r1.name)  # 实例化后，变量首先寻找实例变量，找不到再找类变量
    r1.shot()
    Role.n = '234'
    Role.age = 10  # 增加类变量,存在类的内存里，实例里可以先引用但没法改变
    print(r1.n, r1.age)  # 实例中引用类变量
    r1.age = r1.age + 12  # 等价于增加实例变量r1.m，r1.m=Role.m+12
    r2 = Role('xiaohong', 'bad guy', 'reful')
    r2.age = r2.age + 1  # 等价于增加实例变量r2.m，r2.m=Role.m+1
    print(Role.age, r1.age, r2.age)
    Role.age = 15
    print(Role.age, r1.age, r2.age)
    r1.money = 100  # 实例增加新的变量，只增加在该实例里
    # print(r2.q)# 报错
    Role.state = 'living'
    # del r1.state # r1还没有增加state，不能删除
    del Role.state

#   python 02   类的继承
'''
继承：class 派生类名(基类名[基类组名])
      class C(A, B):   # 继承类 A 和 B 继承多个类
    在python中继承中的一些特点：
    1、如果在子类中需要父类的构造方法就需要显示的调用父类的构造方法，或者不重写父类的构造方法。
    2、在调用基类的方法时，需要加上基类的类名前缀，且需要带上 self 参数变量。区别在于类中调用普通函数时并不需要带上 self 参数
    3、Python 总是首先查找对应类型的方法，如果它不能在派生类中找到对应的方法，它才开始到基类中逐个查找。
    （先在本类中查找调用的方法，找不到才去基类中找）。
    如果在继承元组中列了一个以上的类，那么它就被称作"多重继承" 。
'''
if (x == 1):
    class Parent:  # 定义父类
        parentAttr = 100

        def __init__(self):
            print("调用父类构造函数")

        def parentMethod(self):
            print('调用父类方法')

        def setAttr(self, attr):
            Parent.parentAttr = attr

        def getAttr(self):
            print("父类属性 :", Parent.parentAttr)


    class Child(Parent):  # 定义子类
        def __init__(self):  # 重写了子类的构造函数，就不会再调用父类的构造函数
            print("调用子类构造方法")

        def childMethod(self):
            print('调用子类方法')
            Parent.parentMethod(self)  # 在子类中调用父类方法


    c = Child()  # 实例化子类
    c.childMethod()  # 调用子类的方法
    c.parentMethod()  # 在程序中调用父类方法
    c.setAttr(200)  # 再次调用父类的方法 - 设置属性值
    c.getAttr()  # 再次调用父类的方法 - 获取属性值

#   python 03   类的方法和重写
'''
类的方法
    在类的内部，使用 def 关键字可以为类定义一个方法，与一般函数定义不同，类方法必须包含参数 self,且为第一个参数
类的私有方法
    __private_method：两个下划线开头，声明该方法为私有方法，不能在类的外部调用。
    在类的内部调用 self.__private_methods
    
__foo__: 定义的是特殊方法，也称魔法方法，一般是系统定义名字 ，类似 __init__() 之类的。
        也可以用于重载
'''
if (x==1):
    class Parent1:  # 定义父类
        def myMethod(self):
            print('调用父类方法')


    class Child1(Parent1):  # 定义子类
        def myMethod(self):
            print('调用子类方法')


    c = Child1()  # 子类实例
    c.myMethod()  # 子类调用重写方法


    class Vector:
        def __init__(self, a, b):
            self.a = a
            self.b = b

        def __str__(self):
            return 'Vector (%d, %d)' % (self.a, self.b)
            # 会在调用print的时候打印return中的内容

        def __add__(self, other):
            return Vector(self.a + other.a, self.b + other.b)


    v1 = Vector(2, 10)
    v2 = Vector(5, -2)
    print(v1 + v2)

#   python 04   静态方法和类方法
# 普通方法
if (x==1):
    class dog:
        def __init__(self,name):
            self.name = name

        def eat(self,food):
            self.food = food
            print(self.name,'eat',self.food)

    hashiqi = dog('hashiqi')
    hashiqi.eat('anything')
# 静态方法
if (x==1):
    class dog2:
        color = '白色的'
        def __init__(self,name):
            self.name = name

        #   在使用静态方法时，类中的self将不会再进行传值，此时，静态方法已经和类没什么关系了
        #   不过，静态方法可以用类进行调用，也可以实例化用实例调用
        #   静态方法中使用的参数，可以是外部参数，也可以是类的变量，只要不是self变量
        @staticmethod
        def eat(food):
            # self.food = food  # 报错，因为没有self
            # print(self.name,'eat',self.food) # 报错
            print('这只狗能吃',food)

        @staticmethod
        def looklike(dog2):
            # self.food = food  # 报错，因为没有self
            # print(self.name,'eat',self.food) # 报错
            print('这只狗看起来是', dog2.color)

    hashiqi = dog2('hashiqi')
    hashiqi.eat('anything')
    dog2.eat('大骨头')
    hashiqi.looklike(dog2)  # 报错 必须加dog2 ，需要传入变量，这里的变量是类的变量
# 类方法
if (x==2):
    class dog3:
        food = '大骨头'
        def __init__(self,name):
            self.name = name

        #   类方法只能访问类变量，不能访问实例变量
        #   类方法可以用类调用，参数只能是类变量
        @classmethod
        def eat(dog): # 这里的dog指代自己dog3,
            # self.food = food  # 报错，因为没有self
            # print(self.name,'eat',self.food) # 报错
            print('这只狗能吃',dog.food)

    class dog4():
        food = '肉肉'

        @classmethod
        def eat(dog):
            # self.food = food  # 报错，因为没有self
            # print(self.name,'eat',self.food) # 报错
            print('这只狗能吃', dog.food)

    hashiqi = dog3('hashiqi')
    # hashiqi.eat('anything') # 报错
    # hashiqi.eat(dog3) # 报错
    dog3.eat() # 不需要在外部调用时在传入参数，它访问的是自己类的变量
    dog4.eat()
    # dog3.eat(dog4) #这个当然是不行的，不能访问另一个类的变量，就算是父类或者子类