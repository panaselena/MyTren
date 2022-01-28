import random
# d=open('file.txt','w')
# d.write('Hello World')
# d.close()
import random
d2=open('file1.txt','w',encoding='utf-8')
rand=random.randint(10,1000)
u=str(rand)
d2.write(u)
d2.close()

d3=open('file.txt','w+b')
u_b=int(u)
print(u_b,type(u_b))
b=u_b.to_bytes(4,'big')
# b_e=b.decode()
# print(b_e,'b_e')
b1=u_b.to_bytes(4,'little')
print(b,'b',type(b))
print(b1,'b1',type(b1))
t=tuple(b)
t1=tuple(b1)
print(t,'t',type(t))
print(t1,'t1',type(t1))
d3.write(b)
d3.write(b1)

d3.close()

with open('file.txt','rb') as file:
    g=int.from_bytes(b,'big')
    g1=int.from_bytes(b1,'little')
    print(g, 'g')
    print(g1, 'g1')

