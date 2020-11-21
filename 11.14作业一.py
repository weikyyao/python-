a=["adam","LISA","barT"]

def f(x):
    return x[0].upper()+x[1:].lower()

b=map(f,a)

c=[]
for i in b:
    c.append(i)
print ("规范名字是：",c)