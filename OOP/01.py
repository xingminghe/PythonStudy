class Student():
    def __init__(self,name="junjun", age=19):
        self.name = name
        self.age = age

    def say(self):
        print("my name is {0},i am {1} years old.".format(self.name, self.age))

def sayHello():
    print("欢迎来到图灵学院")
#
if __name__ == '__main__':
    print("我是一个模块")