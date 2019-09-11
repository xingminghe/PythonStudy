# encoding: utf-8
from collections import namedtuple

person = ('name', 'age', 'sex', 'mail')
Person = namedtuple('Person', person)

p = Person('changyubiao', 18, "male", '931367095@qq.com')

print (p.name, p.age, p.mail, p.sex)

for i in range(0, 4):
    print (p[i])
