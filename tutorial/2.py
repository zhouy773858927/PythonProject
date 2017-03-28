# 类型
# int #整数
# float #浮点数
# str #字符串
# bool #布尔值 True False
#
#
# set() #集合
# list [] 数组:数据的集合
# a = [1,True,"156",4.5,5]

# [1, True, '156', 4.5, 5]
# print(a)
# tuple () 元组:数据的集合   **元组的数据是不可变的
# a = (1,2,3,4,5)
# (1, 2, 3, 4, 5)
# print(a)


# 0 a  a[c-'a']+=1
# 1 b
m = {}
print(m.keys())
# dict_keys(['asd', 'Asd'])
# 1
# dict(map) {} 字典(映射): key->value

s="this is a test string"

for i in s: #i=t
    if(i in m.keys()):
        m[i]+=1
    else:
        m[i] = 1
for k in m.keys():
    print(k,m[k])



# a = 1
# b = 1.5
#
# c = 'he say "asdasd"'
# he say "asdasd"
# 占位符  格式化字符串
# " " %
# %d 数      digit
# %s 字符串  string
name = "bob"
age = 25

print("his name is %s ,and his age is %d" % (name,age))





# set()
# 占位符
# 数字 %d
# 字符串 %s

# 数组 [] 可变
# 元组 () 不可变
#  map {} key-value
# 切片
