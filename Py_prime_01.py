# _*_ coding: utf-8 _*_
# 开发人员：Lance_wllz
# 开发人员 86186
# 开发时间 2019/8/2211:10
# 文件名称 Py_prime_01
# 开发工具:PyCharm


# # 01 pycharm 的基本设置
'''
    签名设置 编译器设置 断点运行
'''

# # 02 python 数据类型，Numbers数字 String字符串 List列表 Tuple元祖 Dictionary字典
# #    python 支持四种不同的数字类型 int long float complex python3中long 被移除
# #    https://www.runoob.com/python/python-variable-types.html
x = 2
if (x == 1):
    import sys

    a = 1111111111111111111111111112222222222222222222222222223333333333333333333333333444444444444444444444444
    print('a的类型', type(a))
    print('a int 的字节大小*8', sys.getsizeof(a))
    print('0 int 的字节大小*8', sys.getsizeof(0))
    b = -0.1111111111111111111111111112222222222222222222222222223333333333333333333333333444444444444444444444444
    print('b的类型', type(b))
    print('b float 的字节大小*8', sys.getsizeof(b))
    c = complex(1, 1)  # 创建复数
    print('创建复数', c)
    '''
         int 类型在python中是动态长度，因为python3中int类型是长整型
         print('a int 的字节大小',sys.getsizeof(a)) 输出28
         print('0 int 的字节大小',sys.getsizeof(0)) 输出24
    '''
    a_tuple = (1, 2, 3, 4)  # 括号输入的是序列
    print('元组a_tuple', a_tuple, '类型', type(a_tuple))
    b_list = list(a_tuple)
    print('列表b_tuple', b_list, '类型', type(b_list))

    # zip 用于组合列表成元组的列表 然后变成字典 https://www.runoob.com/python/python-func-zip.html
    a = ['a', 'b', 'c', 'd']
    b = [1, 2, 3, 4]
    c = dict(zip(a, b))
    print('zip c', c)

    # # python 数据和进制转换
    a = 8
    b = str(a)
    c = repr(a)  # repr 用于重构后方便显示 这里没太搞懂
    print('b', b, 'type b', type(b))
    print('c', c, 'type c', type(c))
    print('eval 用于执行字符串表达式', eval('a*2'))  # 字符串内的表达式
    print('十六进a', hex(a))
    print('八进a', oct(a))
    print('二进a', bin(a))

# # 03 python 的存储机制  可变对象和不可变对象
'''
可变对象：对象存放在地址中的值不会被改变（所谓的改变是创建了一块新的地址并把新的对象的值放在新地址中原来的对象并没有发生变化）
不可变对象：对象存放在地址中的值会原地改变
int str float tuple 都属于不可变对象 其中tuple有些特殊（下文解释） 
dict set list 属于可变对象
'''
if (x == 1):
    a = 2.0
    b = 2.0
    print('a 的地址', id(a))  # a 和b的地址是一样的
    print('b 的地址', id(b))
    # 在除了tuple的不可变变量中，只要两个变量的数据类型相同并且值也相等，那么这两个变量的地址也相同
    a1 = [1, 2, 3, 4]
    a2 = a1  # 引用传递
    a3 = a1[:]  # 拷贝
    print('a1 id', id(a1))
    print('a2 id', id(a2))  # list 等号赋值地址是一样的，修改a2 a1会变化，除非用copy
    print('a3 id', id(a3))  # a3 的地址和a1不同
    a2[0] = 10
    print('a1', a1)
    print('a2', a2)
    a2 += [4]  # 和a2=a2+4 不同 +=4 地址不变 相当于调用a2.extend([4])，a2地址没变，所以a1页跟着变化
    # a2 = a2+[4] # 用+ 号时，是重新开辟了地址空间，因此a2 变了，但a1没有改变 a2的地址变了
    print('a1', a1, id(a1))
    print('a2', a2, id(a2))

# # 04 python 运算符 + - * / %取模 **幂次 //取整 python3 整数除以整数会得到小数
'''
    python 位运算符 & | ^异或 ~取反  <<左移（高位溢出丢弃，低位补零）  >>右移
    python 逻辑运算符 and or not
    python 成员运算符 in      not in 判断是否在元组 列表 字典里
    python 身份运算符 is      is not 是判断两个标识符是不是引用自一个对象（判断两个元素是否同一个内存地址） 大于== 号 ==只判断内容
    https://www.runoob.com/python/python-operators.html
'''
'''Python 中没有 ++ 或 -- 自运算符
    a = 1
    a += 1
    在 C/java 之类的语言中，把 a 指向内存地址单元数据值由 1 改成了 2。
    但是在 Python 中是完全不同的另一套机制。
    解释器创建一个新的整数对象 2。
    然后把这个对象的地址再次分配给 a。
 '''

# # 05 python 条件语句
'''如果and 前的条件已经满足，and后的条件不在执行判断，就是条件有错也不抱'''
if (x == 1):
    a = 0
    b = 1
    if (a > 0) and (b / a > 2):
        print("yes")
    else:
        print("no")
    '''简单语句一行搞定'''
    a = [1, 2, 3]
    b = a if len(a) != 0 else ""
    print(b)
    '''消除重复个数'''
    nums = [1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3]
    exist_nums = {}
    point = 0
    for num in nums:
        if num not in exist_nums:
            exist_nums[num] = True
            nums[point] = num
            point += 1
    print(nums[:-1])  # 切片 x：y  不包括第y个元素
    del nums[point:-1]
    del nums[-1]
    print('num_of_dup', point)
    print('dedup', exist_nums)
    print('nums', nums)

# # 06 python 循环语句
'''
    break 在语句块执行中终止循环，并跳出整个循环
    continue 在语句块中终止当前循环，跳出那次循环，执行下一次循环
    pass 空语句
'''
'''八皇后问题 92种解 注意二维列表深拷贝和浅拷贝的，全局变量使用，染色和反染色'''
if (x == 1):
    B = [[0] * 8 for i in range(8)]
    A = B.copy()
    C = [[0] * 8 for i in range(8)]
    cur = 0
    Q = 0


    def queen_test(A, cur, C):
        # print('cur', cur)
        if cur < 8:
            for col in range(8):
                if A[cur][col] == 0:
                    # print('cur', cur, 'col', col)
                    if cur == 7:
                        A[cur][col] = A[cur][col] + 1
                        C[cur][col] = C[cur][col] + 1
                        global Q
                        Q = Q + 1
                        print('finallA', C)
                        print(Q)
                        A[cur][col] = A[cur][col] - 1
                        C[cur][col] = C[cur][col] - 1

                    else:
                        # 染色模块begin
                        A[cur][col] = A[cur][col] + 1
                        C[cur][col] = C[cur][col] + 1
                        j = 1
                        for i in range(cur + 1, 8):
                            # print('i',i)
                            A[i][col] = A[i][col] + 1
                            if col + j < 8:
                                A[i][col + j] = A[i][col + j] + 1
                            if col - j >= 0:
                                A[i][col - j] = A[i][col - j] + 1
                            j = j + 1
                        # 染色模块end
                        # print("A", A)
                        queen_test(A, cur + 1, C)  # 染色后迭代
                        # 反染色模块
                        A[cur][col] = A[cur][col] - 1
                        C[cur][col] = C[cur][col] - 1
                        j = 1
                        for i in range(cur + 1, 8):
                            # print('i',i)
                            A[i][col] = A[i][col] - 1
                            if col + j < 8:
                                A[i][col + j] = A[i][col + j] - 1
                            if col - j >= 0:
                                A[i][col - j] = A[i][col - j] - 1
                            j = j + 1
                        # 反染色模块end


    queen_test(A, cur, C)
'''八皇后问题 92种解 break 迭代结构，return中断'''
if (x==1):
    Num_of_solution = 0
    def queen_test2(A, cur):
        if cur == len(A):
            global Num_of_solution
            Num_of_solution = Num_of_solution + 1
            print(Num_of_solution)
            print('A', A)
            return 0 # return 会从此中断
        for col in range(len(A)):
            A[cur] = col
            flag = True
            for row in range(cur):
                if A[row] == col or abs(col-A[row]) == cur - row:
                    flag = False
                    break
            if flag:
                queen_test2(A,cur+1)
    queen_test2([None]*8,0)

# # 07 python math·cmath·random ·三角函数（math是实数 cmath是复数）
'''
math
    abs（绝对值）    ceil(上入)    cmp（<返回-1，==返回0，>返回1）   exp(返回e的次幂)
    fabs(返回绝对值) log(以e为底数)  log10(以10为底数)   modf(返回小数,和整数部分)
    power(返回x**y)   round(x[,n]) 给出n值，则代表舎入到小数点后的位数 sqrt(平方根)

random
    random随机生成0-1   choice(seq)从序列元素中随机挑选一个 
    randrange([start],stop,[,step]) 从指定范围内，按指定技术递增的集合中获取一个随机数
    seed([x]) 改变随机数生成器的种子seed
    shuffle(lst)将序列的所有元素随机排列
    uniform（x,y）随机生成x-y范围内的随机数 
三角函数
    hypot（x,y）返回欧几里得范数
    degree 弧度转角度  
    radians（x）角度换弧度
    三角函数处理的都是弧度
'''
if (x==1):
    import math
    print(math.modf(10.23))
    print(16**0.5)


# # 08 python 字符串
'''
字符串格式化
      %c	 格式化字符及其ASCII码
      %s	 格式化字符串
      %d	 格式化整数
      %u	 格式化无符号整型
      %o	 格式化无符号八进制数
      %x	 格式化无符号十六进制数
      %X	 格式化无符号十六进制数（大写）
      %f	 格式化浮点数字，可指定小数点后的精度
      %e	 用科学计数法格式化浮点数
      %E	 作用同%e，用科学计数法格式化浮点数
      %g	 %f和%e的简写
      %G	 %f 和 %E 的简写
      %p	 用十六进制数格式化变量的地址
    https://www.runoob.com/python3/python3-string.html
'''
'''
字符串操作
    1	capitalize() 
    将字符串的第一个字符转换为大写
    2   center(width, fillchar)
    返回一个指定的宽度 width 居中的字符串，fillchar 为填充的字符，默认为空格。
    3	count(str, beg= 0,end=len(string))
    返回 str 在 string 里面出现的次数，如果 beg 或者 end 指定则返回指定范围内 str 出现的次数
    4	bytes.decode(encoding="utf-8", errors="strict")
    Python3 中没有 decode 方法，但我们可以使用 bytes 对象的 decode() 方法来解码给定的 bytes 对象，
    这个 bytes 对象可以由 str.encode() 来编码返回。
    5	encode(encoding='UTF-8',errors='strict')
    以 encoding 指定的编码格式编码字符串，如果出错默认报一个ValueError 的异常，除非 errors 指定的是'ignore'或者'replace'
    6	endswith(suffix, beg=0, end=len(string))
    检查字符串是否以 obj 结束，如果beg 或者 end 指定则检查指定的范围内是否以 obj 结束，如果是，返回 True,否则返回 False.
    7	expandtabs(tabsize=8)
    把字符串 string 中的 tab 符号转为空格，tab 符号默认的空格数是 8 。
    8	find(str, beg=0, end=len(string))
    检测 str 是否包含在字符串中，如果指定范围 beg 和 end ，则检查是否包含在指定范围内，如果包含返回开始的索引值，否则返回-1
    9	index(str, beg=0, end=len(string))
    跟find()方法一样，只不过如果str不在字符串中会报一个异常.
    10	isalnum()
    如果字符串至少有一个字符并且所有字符都是字母或数字则返 回 True,否则返回 False
    11	isalpha()
    如果字符串至少有一个字符并且所有字符都是字母则返回 True, 否则返回 False
    12	isdigit()
    如果字符串只包含数字则返回 True 否则返回 False..
    13	islower()
    如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是小写，则返回 True，否则返回 False
    14	isnumeric()
    如果字符串中只包含数字字符，则返回 True，否则返回 False
    15	isspace()
    如果字符串中只包含空白，则返回 True，否则返回 False.
    16	istitle()
    如果字符串是标题化的(见 title())则返回 True，否则返回 False
    17	isupper()
    如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是大写，则返回 True，否则返回 False
    18	join(seq)
    以指定字符串作为分隔符，将 seq 中所有的元素(的字符串表示)合并为一个新的字符串
    19	len(string) 
    返回字符串长度
    20	ljust(width[, fillchar])
    返回一个原字符串左对齐,并使用 fillchar 填充至长度 width 的新字符串，fillchar 默认为空格。
    21	lower()
    转换字符串中所有大写字符为小写.
    22	lstrip()
    截掉字符串左边的空格或指定字符。
    23	maketrans()
    创建字符映射的转换表，对于接受两个参数的最简单的调用方式，第一个参数是字符串，表示需要转换的字符，
    第二个参数也是字符串表示转换的目标。
    24	max(str)
    返回字符串 str 中最大的字母。
    25	min(str)
    返回字符串 str 中最小的字母。
    26	replace(old, new [, max])
    把 将字符串中的 str1 替换成 str2,如果 max 指定，则替换不超过 max 次。
    27	rfind(str, beg=0,end=len(string))
    类似于 find()函数，不过是从右边开始查找.
    28	rindex( str, beg=0, end=len(string))
    类似于 index()，不过是从右边开始.
    29	rjust(width,[, fillchar])
    返回一个原字符串右对齐,并使用fillchar(默认空格）填充至长度 width 的新字符串
    30	rstrip()
    删除字符串字符串末尾的空格.
    31	split(str="", num=string.count(str))
    num=string.count(str)) 以 str 为分隔符截取字符串，如果 num 有指定值，则仅截取 num+1 个子字符串
    32	splitlines([keepends])
    按照行('\r', '\r\n', \n')分隔，返回一个包含各行作为元素的列表，如果参数 keepends 为 False，不包含换行符，
    如果为 True，则保留换行符。
    33	startswith(substr, beg=0,end=len(string))
    检查字符串是否是以指定子字符串 substr 开头，是则返回 True，否则返回 False。如果beg 和 end 指定值，则在指定范围内检查。
    34	strip([chars])
    在字符串上执行 lstrip()和 rstrip()
    35	swapcase()
    将字符串中大写转换为小写，小写转换为大写
    36	title()
    返回"标题化"的字符串,就是说所有单词都是以大写开始，其余字母均为小写(见 istitle())
    37	translate(table, deletechars="")
    根据 str 给出的表(包含 256 个字符)转换 string 的字符, 要过滤掉的字符放到 deletechars 参数中
    38	upper()
    转换字符串中的小写字母为大写
    39	zfill (width)
    返回长度为 width 的字符串，原字符串右对齐，前面填充0
    40	isdecimal()
    检查字符串是否只包含十进制字符，如果是返回 true，否则返回 false。
'''
if (x==1):
    print('0','\\') #但斜杠
    print('1','\b','1.1') #退格
    print('2','\000','2.2')#空
    print('3','\n') #换行
    print('4','\v','4.1') # 纵向制表符
    print('5','\t','5.1') # 横向制表符
    print('6','\r','6.1') #回车
    print('7','\f','7.1') #换页
    print(chr(ord('a')+1)) #chr转ascii 与ascii转chr python里没有char类型

# # 09 python 列表
'''
相关后置命令
    1	list.append(obj)
    在列表末尾添加新的对象
    2	list.count(obj)
    统计某个元素在列表中出现的次数
    3	list.extend(seq)
    在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
    4	list.index(obj)
    从列表中找出某个值第一个匹配项的索引位置
    5	list.insert(index, obj)
    将对象插入列表
    6	list.pop([index=-1])
    移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
    7	list.remove(obj)
    移除列表中某个值的第一个匹配项
    8	list.reverse()
    反向列表中元素
    9	list.sort( key=None, reverse=False)
    对原列表进行排序
    10	list.clear()
    清空列表
    11	list.copy()
    复制列表
注意点
    二维列表的列表深拷贝和浅拷贝
'''
if (x==1):
    #一维列表copy和二维的不同
    #copy是浅复制，修改列表不会相互影响，但是修改列表里的对象(对象是列表或字典)会相互影响
    a = [1, 2, 3, 4]
    c = [1, 2, 3, 3]
    print(id(a),id(a[0]),id(a[1]),id(a[2]),id(a[3])) #a存的是列表地址，连续一串内存里存放着a[0]~a[1]，a[1]存的是int‘2’的地址
    print(id(c),id(c[0]), id(c[1]), id(c[2]), id(c[3])) # python 的内存管理机制，不会为相同的内容多分配内存
    b = a.copy() # 为b开辟新地址空间，b!=a,b[0]存放的东西和a[0]一样，是int(1)的地址
    a[0] = 2 #修改了a[0]的内容，是让a[0] 存放int(2)的地址
    print('a id',id(a),id(a[0]),id(a[1]),id(a[2]),id(a[3]))
    print('b id',id(b), id(b[0]),id(b[1]),id(b[2]),id(b[3]))

    # copy是浅复制，修改列表里的对象(对象是列表或字典)会相互影响如下
    k = [1, 2, 3]
    a = [[1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]]    # a[0]存的是列表地址，连续一串内存里存放着a[0][0]~a[0][1] a[0][0]存着int(1)地址
                                                        # a是二维列表地址，连续一串内存里存着a[0]~a[1]
    c = [[1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]]
    d = a
    b = a.copy()  # 为b开辟新地址空间，b!=a ,b[0]=a[0],b[0]存放的东西和a[0]一样,是列表地址，连续一串内存里存放着a[0][0]~a[0][1]
                  # 因为存放的是列表地址，所以更改a[0][0]，a[0]和b[0]不改变，所以b[0][0]=a[0][0],所以b[0][0]也会改变
    print('kid',id(k),id(k[0]),id(k[1]),id(k[2]))
    print('aid',id(a),id(a[0]), id(a[1]), id(a[2]), id(a[3]))
    print('did', id(d), id(d[0]), id(d[1]), id(d[2]), id(d[3]))
    print('cid',id(c), id(c[0]), id(c[1]), id(c[2]), id(c[3]))
    print('aid', id(a),id(a[0]), id(a[0][0]), id(a[0][1]), id(a[0][2]))
    print('cid', id(c),id(c[0]), id(c[0][0]), id(c[0][1]), id(c[0][2]))
    print('bid', id(b),id(b[0]), id(b[0][0]), id(b[0][1]), id(b[0][2]))
    a[0][0] = 2
    print('a', a, 'a[0]id', id(a[0]), 'a[0][0]id', id(a[0][0]))
    print('b', a, 'b[0]id', id(b[0]), 'b[0][0]id', id(b[0][0]))
    # 使用deepcopy 深拷贝可以改变
    import copy as CP
    e = CP.deepcopy(a)
    print('eid', id(e), id(e[0]), id(e[0][0]), id(e[0][1]), id(e[0][2])) # e！=a，e[0]!=a[0],所以a[0][0]改变，e[0][0]不变


    # ([]*x)列表生成式浅拷贝  for i in range（x）是深拷贝
    a = [[1,2,3]]*4 # 注意和[[1,2,3]*4]的区别 二维列表里面保存的是一维列表的地址 这是列表内的浅拷贝，
                    # [[1,2,3]]*4把[1,2,3]的地址复制了4遍，a[0]=a[1]=a[2]=a[3]都是一个列表地址，
                    # 修改a[0][1],a[1][1]也会改变
                    # [[i for i in range(3)]]*4 也是列表内的浅拷贝 *和append(same)都是浅拷贝
    print('aid',id(a),id(a[0]), id(a[1]), id(a[2]), id(a[3]))
    # for i in range（x）是深拷贝
    a = [[1, 2, 3] for i in range(4)]  # 列表内开辟独立地址分布存放4个[1,2,3]
    print('aid', id(a), id(a[0]), id(a[1]), id(a[2]), id(a[3]))

    import copy as CP
    a = [[1,2,3]]*4
    e = CP.deepcopy(a)
    print('aid', id(a), id(a[0]), id(a[1]), id(a[2]), id(a[3]))
    print('eid', id(e), id(e[0]), id(e[1]), id(e[2]), id(e[3])) # 改变a[0][0] e[0][0]不变，改变e[0][0]，e[1][0]会变
    e[0][0]=5
    print(e)

    k = [1,2,3]
    a=[[[1,2,3],[1,2,3]],[[1,2,3],[1,2,3]]] # 三维列表
    b=a.copy()
    print('kid', id(k), id(k[0]), id(k[1]), id(k[2]))
    print('aid',id(a),id(a[0]), id(a[1]))
    print('aid', id(a[0]), id(a[0][0]), id(a[0][1]))
    print('aid', id(a[0][0]), id(a[0][0][0]), id(a[0][0][1]),id(a[0][0][2]))
    print('bid', id(b), id(b[0]), id(b[1]))
    print('bid', id(b[0]), id(b[0][0]), id(b[0][1]))
    import copy as CP
    e = CP.deepcopy(a)
    print('eid', id(e), id(e[0]), id(e[1]))
    print('eid', id(e[0]), id(e[0][0]), id(e[0][1])) # 深拷贝适用于任意维度的数组列表拷贝

# # 10 python map函数 zip函数  lamda 函数
'''
    zip() 函数用于将可迭代的对象(序列，函数)作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。
    如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，利用 * 号操作符，可以将元组解压为列表。
'''
if (x==1):
    a = [1,2,3]
    b = [4,5,6]
    c = [4,5,6,7,8]
    d = (zip(a,b))  # python3 中返回的是一个支持遍历的对象，需要手动list化才能显示出来
    e = zip(a,c)    # 以最短的序列为基准进行打包
    print(d)
    print(list(d))
    print(list(e))
    f = zip(*e)     # list(d) 执行后d变为list 就无法解压了
    print(list(f))

    # g = lambda x:f(x)  输入x 输出f(x) lambda就是一个返回值，可以存在于任意值存在的地方，如列表，字典
    # 匿名函数，在需要函数但是又不能或者不想定义函数时使用
    # lambda 可以赋给变量，函数，函数返回值，作为参数传递给调用者
    g = lambda x, y, z: x + y + z
    print(g(1, 2, 3))
    L = [lambda x: x + 2, lambda x: x * 2, lambda x: x ** 2]
    print("L=", L[0](1), L[1](2), L[2](3))
    k = lambda *args: sum(args)     # 输入是任意个数的参数，输出是它们的和(隐性要求是输入参数必须能够进行加法运算)
    # 由于在args变量前有 * 前缀 ，所有多余的函数参数都会作为一个元组存储在args中 。
    # 如果使用的是 ** 前缀 ，多余的参数则会被认为是一个字典的健 / 值对
    print(k(1,2,3,4,5,6))
    m = lambda x: lambda y: x*2+y + 1   # lambda 嵌套 不过感觉没啥必要
    print(m(2)(5))

    # map的语法是 map(function, iterable, ...)
    a = map(lambda x:x**2, [1, 2, 3, 4, 5])  # 计算列表各个元素的平方 返回的也是一个支持遍历的对象，需要手动list化
    print(list(a))

# # 11 python 时间元组
'''

'''
if (x==1):
    import time
    localtime = time.localtime(time.time())
    print("本地时间为 :", localtime)
    # 时间格式化
    # 格式化成2016-03-20 11:45:39形式
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    # 格式化成Sat Mar 28 22:24:24 2016形式
    print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))
    # 将格式字符串转换为时间戳
    a = "Sat Mar 28 22:24:24 2016"
    print(time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y")))


# # 12 python try except enumerate
'''
try 和except的用法
    异常名称	描述
    BaseException	所有异常的基类
    SystemExit	解释器请求退出
    KeyboardInterrupt	用户中断执行(通常是输入^C)
    Exception	常规错误的基类
    StopIteration	迭代器没有更多的值
    GeneratorExit	生成器(generator)发生异常来通知退出
    StandardError	所有的内建标准异常的基类
    ArithmeticError	所有数值计算错误的基类
    FloatingPointError	浮点计算错误
    OverflowError	数值运算超出最大限制
    ZeroDivisionError	除(或取模)零 (所有数据类型)
    AssertionError	断言语句失败
    AttributeError	对象没有这个属性
    EOFError	没有内建输入,到达EOF 标记
    EnvironmentError	操作系统错误的基类
    IOError	输入/输出操作失败
    OSError	操作系统错误
    WindowsError	系统调用失败
    ImportError	导入模块/对象失败
    LookupError	无效数据查询的基类
    IndexError	序列中没有此索引(index)
    KeyError	映射中没有这个键
    MemoryError	内存溢出错误(对于Python 解释器不是致命的)
    NameError	未声明/初始化对象 (没有属性)
    UnboundLocalError	访问未初始化的本地变量
    ReferenceError	弱引用(Weak reference)试图访问已经垃圾回收了的对象
    RuntimeError	一般的运行时错误
    NotImplementedError	尚未实现的方法
    SyntaxError	Python 语法错误
    IndentationError	缩进错误
    TabError	Tab 和空格混用
    SystemError	一般的解释器系统错误
    TypeError	对类型无效的操作
    ValueError	传入无效的参数
    UnicodeError	Unicode 相关的错误
    UnicodeDecodeError	Unicode 解码时的错误
    UnicodeEncodeError	Unicode 编码时错误
    UnicodeTranslateError	Unicode 转换时错误
    Warning	警告的基类
    DeprecationWarning	关于被弃用的特征的警告
    FutureWarning	关于构造将来语义会有改变的警告
    OverflowWarning	旧的关于自动提升为长整型(long)的警告
    PendingDeprecationWarning	关于特性将会被废弃的警告
    RuntimeWarning	可疑的运行时行为(runtime behavior)的警告
    SyntaxWarning	可疑的语法的警告
    UserWarning	用户代码生成的警告

enumerate的用法 列举序列的内容的序号(从0开始)和内容值
'''
if (x==1):
    sequence = [12, 34, 34, 23, 45, 76, 89]
    for i, j in enumerate(sequence):
        print(i,j)

# # 12 python 迭代器和生成器
'''
    迭代器是一个可以记住遍历的位置的对象。
    迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。
    迭代器有两个基本的方法：iter() 和 next()。
    在 Python 中，使用了 yield 的函数被称为生成器（generator）。
    
    跟普通函数不同的是，生成器是一个返回迭代器的函数，只能用于迭代操作，更简单点理解生成器就是一个迭代器。
    在调用生成器运行的过程中，每次遇到 yield 时函数会暂停并保存当前所有的运行信息，返回 yield 的值, 并在下一次执行 next() 方法时从当前位置继续运行。
    调用一个生成器函数，返回的是一个迭代器对象。
'''
if (x==1):
    import sys  # 引入 sys 模块
    list = [1, 2, 3, 4]
    it = iter(list)  # 创建迭代器对象
    while True:
        try:
            print(next(it))
        except StopIteration:
            sys.exit()
if (x==1):
    import sys
    def fibonacci(n):  # 生成器函数 - 斐波那契
        a, b, counter = 0, 1, 0
        while True:
            if (counter > n):
                return
            yield a
            a, b = b, a + b
            counter += 1
    f = fibonacci(10)  # f 是一个迭代器，由生成器返回生成
    while True:
        try:
            print(next(f), end=" ")
        except StopIteration:
            sys.exit()

# # 13 python 中的包
'''
python中的包就是指一类含有脚本的文件夹，该文件夹中需要有__init__.py 文件，此外该文件夹中可以有多个其他py文件，多个
子文件夹（子包）
如层次结构：
test.py
package_runoob
|-- __init__.py
|-- runoob1.py
|-- runoob2.py
https://www.runoob.com/python/python-modules.html

通俗的理解 __name__ == '__main__'：
假如你叫小明.py，在朋友眼中，你是小明(__name__ == '小明')；在你自己眼中，你是你自己(__name__ == '__main__')。
if __name__ == '__main__'的意思是：当 .py 文件被直接运行时，if __name__ == '__main__' 之下的代码块将被运行；
 当 .py 文件以模块形式被导入时，if __name__ == '__main__'之下的代码块不被运行
'''

# # 14 python的常用函数和内置函数
'''
    系统相关的信息模块: import sys
        sys.argv 是一个 list,包含所有的命令行参数.    
        sys.stdout sys.stdin sys.stderr 分别表示标准输入输出,错误输出的文件对象.    
        sys.stdin.readline() 从标准输入读一行 sys.stdout.write("a") 屏幕输出a    
        sys.exit(exit_code) 退出程序    
        sys.modules 是一个dictionary，表示系统中所有可用的module    
        sys.platform 得到运行的操作系统环境    
        sys.path 是一个list,指明所有查找module，package的路径.  
        操作系统相关的调用和操作: import os
        os.environ 一个dictionary 包含环境变量的映射关系   
        os.environ["HOME"] 可以得到环境变量HOME的值     
        os.chdir(dir) 改变当前目录 os.chdir('d:\\outlook')   
    注意windows下用到转义     
        os.getcwd() 得到当前目录     
        os.getegid() 得到有效组id os.getgid() 得到组id     
        os.getuid() 得到用户id os.geteuid() 得到有效用户id     
        os.setegid os.setegid() os.seteuid() os.setuid()     
        os.getgruops() 得到用户组名称列表     
        os.getlogin() 得到用户登录名称     
        os.getenv 得到环境变量     
        os.putenv 设置环境变量     
        os.umask 设置umask     
        os.system(cmd) 利用系统调用，运行cmd命令   
    内置模块(不用import就可以直接使用)常用内置函数：
        help(obj) 在线帮助, obj可是任何类型    
        callable(obj) 查看一个obj是不是可以像函数一样调用    
        repr(obj) 得到obj的表示字符串，可以利用这个字符串eval重建该对象的一个拷贝    
        eval_r(str) 表示合法的python表达式，返回这个表达式    
        dir(obj) 查看obj的name space中可见的name    
        hasattr(obj,name) 查看一个obj的name space中是否有name    
        getattr(obj,name) 得到一个obj的name space中的一个name    
        setattr(obj,name,value) 为一个obj的name   
        space中的一个name指向vale这个object    
        delattr(obj,name) 从obj的name space中删除一个name    
        vars(obj) 返回一个object的name space。用dictionary表示    
        locals() 返回一个局部name space,用dictionary表示    
        globals() 返回一个全局name space,用dictionary表示    
        type(obj) 查看一个obj的类型    
        isinstance(obj,cls) 查看obj是不是cls的instance    
        issubclass(subcls,supcls) 查看subcls是不是supcls的子类  
    
    ##################    类型转换  ##################
    
    chr(i) 把一个ASCII数值,变成字符    
    ord(i) 把一个字符或者unicode字符,变成ASCII数值    
    oct(x) 把整数x变成八进制表示的字符串    
    hex(x) 把整数x变成十六进制表示的字符串    
    str(obj) 得到obj的字符串描述    
    list(seq) 把一个sequence转换成一个list    
    tuple(seq) 把一个sequence转换成一个tuple    
    dict(),dict(list) 转换成一个dictionary    
    int(x) 转换成一个integer    
    long(x) 转换成一个long interger    
    float(x) 转换成一个浮点数    
    complex(x) 转换成复数    
    max(...) 求最大值    
    min(...) 求最小值  
'''

# # 15 python   I/O命令 和file方法 查看网站
'''
open(file_name,mode)    close   write   read
tell()方法告诉你文件内的当前位置, 换句话说，下一次的读写会发生在文件开头这么多字节之后。
seek（offset [,from]）方法改变当前文件的位置。Offset变量表示要移动的字节数。From变量指定开始移动字节的参考位置。
如果from被设为0，这意味着将文件的开头作为移动字节的参考位置。如果设为1，则使用当前的位置作为参考位置。如果它被设
为2，那么该文件的末尾将作为参考位置。
mkdir()创建新目录     chdir()更改当前目录      getcwd()显示当前工作目录        rmdir()删除目录
'''