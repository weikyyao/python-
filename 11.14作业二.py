from functools import  reduce

x=input("请输入数字：")

def prod(x):
    list=x.split(" ")
    intlist=[int(i) for i in list]
    sum = reduce(lambda x, y: x * y, intlist)
    return sum

sum=prod(x)

print ("列表{0}的乘积是{1}".format([int(i) for i in x.split(" ")],sum))
