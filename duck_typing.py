#OOP Duck Typing

class Duck:
    def walk(self):
        print("鸭子可以走路")
    def talk(self):
        print("鸭子会呱呱叫")

class Chicken:
    def walk(self):
        print("鸡可以走路")
    def talk(self):
        print("鸡会咕咕叫")
#即使没有父与子继承关系,也可以当做同一类型的类别使用
class Person:
    def catch(self,animal):
        animal.walk()
        animal.talk()

person = Person()
duck = Duck()
person.catch(duck)

chicken = Chicken()
person.catch(chicken)
