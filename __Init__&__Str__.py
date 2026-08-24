class Student:
    # Class（类）
    # Student 是一个模板，用来创建学生 Object

    def __init__(self, name, age, score):
        # __init__ = 初始化
        # 创建 Student Object 时会自动执行
        # self = 当前的 Object

        self.name = name
        # self.name = Attribute（属性）
        # 把传进来的 name 储存到这个 Object

        self.age = age
        self.score = score

    def __str__(self):
        return (f"Name: {self.name}\n"
                f"Age: {self.age}\n"
                f"Score: {self.score}")
        # __str__ = 特殊方法 (推荐使用这个)
        # 作用：规定 print(Object) 时，要显示什么文字
        # 必须 return 一个字符串，不能直接 print

        # 有了 __str__ 后：
        # print(student1)
        # Python 会自动调用 student1.__str__()
        # 然后显示 return 回来的字符串

        # 如果没有 __str__：
        # print(student1)
        # 可能会显示：
        # <__main__.Student object at 0x000001C2366BE3F0>
        # 这是 Python 默认的 Object 显示方式，不容易看懂

    def change_name(self, new_name):
        # Method：修改名字
        # new_name 是传进来的新名字

        self.name = new_name
        # 把 Object 原本的名字修改成新名字

        print(self)
        # 可以在一个 Method 里面调用另一个 Method
        # 这里不是必要的，只是修改名字后顺便显示资料


    def add_score(self, amount):
        # Method：增加 / 减少分数
        new_score = self.score + amount
        if new_score < 0:
            print("Score Cant Be Negative")
        else:
            self.score = new_score


# Object（对象）
# 根据 Student Class 创建两个不同的 Object

student1 = Student("Ck", 27, 100)
# student1 是一个 Student Object
# name = Ck
# age = 27
# score = 100

student2 = Student("Lim", 25, 87)
# student2 也是 Student Object
# 但是资料和 student1 独立


student1.add_score(15)
# self = student1
# 100 + 15 = 115

student2.add_score(-30)
# self = student2
# 87 + (-30) = 57


student1.change_name("Kok")
# self = student1
# 把 student1 的名字 Ck 改成 Kok

print(student1)
# 会自动调用 __str__()
