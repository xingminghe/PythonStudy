'''
定义一个学生类，用来形=形容学生

'''
# 定义一个空类
class Student():
    pass
# 定义一个对象
mingyue = Student()

#在定义一个类，用来描述挺python的学生
class PythonStudent():
    name = None
    age = 18
    course = "Python"

    def doHomework(self):
        print("我在做作业")
        return None

junjun = PythonStudent()
print(junjun.age)
print(junjun.name)
junjun.doHomework()
