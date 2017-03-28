# 函数
#       默认参数
#       固定参数
#       不定长参数 *
#       扩展参数   **
# def test(arg1=1,arg2=2,arg3=sadsa)
# def test(1,2,3)
#
#       返回值不定长

#

def test(name="bob",age=25,**aihao):
    '''
    输入一个人的名字和年龄,爱好,并返回
    his name is 名字,his age is 年龄,his love is 爱好
    '''
    # {'xihuan1': '看书', 'xihuan2': '敲代码'} m[key]
    print("his name is %s,his age is %d" % (name,age))
    for i in aihao.keys():
        print("his %s is %s" % (i,aihao[i]))

# test(name="sads",age=15)
# his name is sads,his age is 15
# test(name="ASdas",age=15,xihuan1="看书",xihuan2="敲代码",tebiexihuan="扯淡")
# his name is ASdas,his age is 15
# his tebiexihuan is 扯淡
# his xihuan2 is 敲代码
# his xihuan1 is 看书



# test(name="test",age=15)
# his name is test,his age is 15
# his love is 看书
# his love is 写代码
# his love is 扯淡

# his name is test,his age is 15,his love is ('看书', '写代码', '扯淡')
# his name is test,his age is 15,his love is ('看书', '写代码')
# his name is test,his age is 15,his love is 无爱好
# his name is bob,his age is 25


# his name is bob,his age is 24
# his name is test,his age is 24
# his name is bob,his age is 25
# his name is bob,his age is 25



# f(x)=4x+3
# f(x,y)=4*x+3y
# f(x)
# return datas

# def 关键字
# ()参数 表
# if for while:
# def func_name():
    # do()
    # return something


# def tongjizimugeshu(s):
#     m={}
#     for i in s: #i=t
#         if(i in m.keys()):
#             m[i]+=1
#         else:
#             m[i] = 1
#     return m
#
# testString="sadsa"
# testString2="dsaodhnqowndoiwhjdosi"
# print(tongjizimugeshu(testString2))
# {'a': 2, 's': 2, 'd': 1}
# {'a': 1, 'i': 2, 'd': 4, 'h': 2, 's': 2, 'w': 2, 'q': 1, 'j': 1, 'n': 2, 'o': 4}


# (11, 'test1', 'test2', 'test3')
