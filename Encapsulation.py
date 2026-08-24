# ============================================================
# OOP - Encapsulation（封装）
# ============================================================

# Encapsulation = 封装
#
# 简单来说：
# 把 Object 内部的重要资料保护起来，
# 不让外部随便修改，而是通过 Method 控制资料的修改。
#
#
# 普通情况：
#
# product1.price = -500
#
# 外部可以直接修改 Attribute。
#
# Encapsulation：
#
# self.__price
#
# 让重要的 Attribute 放在 Class 内部，
# 再通过 Method 来控制修改。


# ============================================================
# 1. 普通 Attribute
# ============================================================

class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock


product1 = Product("Laptop", 3500, 10)

# 外部可以直接修改
product1.price = -500

print(product1.price)
# -500


# ============================================================
# 2. 使用 __ 保护 Attribute
# ============================================================

class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.__price = price
        self.stock = stock


# __price 前面有两个 _
#
# self.__price
#
# Python 会进行 Name Mangling（名称改写）
#
# __price
#    ↓
# _Product__price
#
# 所以 __price 和 price 是两个不同的 Attribute。


# ============================================================
# 3. 为什么要使用 __price？
# ============================================================

class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.__price = price
        self.stock = stock

    def change_price(self, new_price):

        if new_price <= 0:
            print("Price must be greater than 0")

        else:
            self.__price = new_price


product1 = Product("Laptop", 3500, 10)

product1.change_price(-500)
# Price must be greater than 0

product1.change_price(4000)
# Price 成功修改成 4000


# ============================================================
# 4. Encapsulation 的概念
# ============================================================

# 不使用 Encapsulation：
#
# 外部
#   ↓
# 直接修改 Attribute
#   ↓
# self.price
#
#
# 使用 Encapsulation：
#
# 外部
#   ↓
# Method
#   ↓
# 检查资料是否合法
#   ↓
# 修改 __price


# ============================================================
# 5. __price 不是绝对不能访问
# ============================================================

# Python 的 __price 并不是 100% Private。
#
# Python 会进行 Name Mangling：
#
# self.__price
#      ↓
# self._Product__price
#
#
# 所以理论上可以：

product1._Product__price

# 但是正常情况下不应该这样做。
#
# 应该使用 Class 提供的 Method：
#
# product1.change_price(4000)
#
#
# 所以 Python 的 Encapsulation 比较像：
#
# "这是内部资料，请通过规定的方法来操作。"
#
# 而不是：
#
# "绝对禁止外部访问。"


# ============================================================
# 6. Attribute 可以后来才创建
# ============================================================

class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.__price = price
        self.stock = stock


product1 = Product("Laptop", 3500, 10)

# 虽然 __init__ 没有 self.price
# 但是 Python 仍然可以后来创建一个新的 Attribute。

product1.price = -400

print(product1.price)
# -400


# 这时候 Object 可以想象成：
#
# product1
# ├── name = "Laptop"
# ├── __price = 3500
# ├── stock = 10
# └── price = -400
#
#
# 注意：
#
# __price != price
#
# 它们是两个不同的 Attribute。


# ============================================================
# 7. 为什么 product1.price 可以出现？
# ============================================================

# Python 不要求所有 Attribute 都必须在 __init__ 里面声明。
#
# __init__ 的作用是：
#
# "Object 创建的时候，初始化哪些 Attribute。"
#
# 而不是：
#
# "Object 以后只能拥有这些 Attribute。"
#
#
# 例如：

product1.color = "Black"
product1.brand = "ASUS"

# 即使 __init__ 没有：
#
# self.color
# self.brand
#
# 也可以后来建立。


# ============================================================
# 8. display() 和 __str__()
# ============================================================

class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.__price = price
        self.stock = stock

    def display(self):
        print(f"Item : {self.name}\n"
              f"Price : RM {self.__price:.2f}\n"
              f"Stock : {self.stock}")

    def __str__(self):
        return (f"Item : {self.name}\n"
                f"Price : RM {self.__price:.2f}\n"
                f"Stock : {self.stock}")


# __str__ 要使用 return
# 因为 print(Object) 需要得到一个 String。


product1 = Product("Laptop", 3500, 10)

print(product1)

# Python 会自动调用：
#
# product1.__str__()


# ============================================================
# 9. Encapsulation + Method
# ============================================================

class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.__price = price
        self.stock = stock

    def change_price(self, new_price):

        if new_price <= 0:
            print("Price must be greater than 0")

        else:
            self.__price = new_price

    def __str__(self):
        return (f"Item : {self.name}\n"
                f"Price : RM {self.__price:.2f}\n"
                f"Stock : {self.stock}")


product1 = Product("Laptop", 3500, 10)

product1.change_price(-500)
# Price must be greater than 0

print(product1)
# Price 仍然是 RM 3500.00

product1.change_price(4000)

print(product1)
# Price 变成 RM 4000.00


# ============================================================
# 10. Encapsulation + Inventory
# ============================================================

class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.__price = price
        self.stock = stock

    def change_price(self, new_price):

        if new_price <= 0:
            print("Price must be greater than 0")
        else:
            self.__price = new_price

    def add_stock(self, amount):
        self.stock += amount

    def remove_stock(self, amount):

        if amount > self.stock:
            return False

        else:
            self.stock -= amount
            return True

    def sell(self, amount):

        if self.remove_stock(amount):
            print(f"Sold {amount} {self.name} Success")

        else:
            print("No Enough Stock")

    def __str__(self):
        return (f"Item : {self.name}\n"
                f"Price : RM {self.__price:.2f}\n"
                f"Stock : {self.stock}")


# ============================================================
# 11. Encapsulation 最重要的概念
# ============================================================

# 普通 Attribute：
#
# self.price
# ↓
# 外部可以直接修改
#
#
# Encapsulation：
#
# self.__price
# ↓
# 内部资料
# ↓
# 通过 Method 控制修改
#
#
# 例如：
#
# product1.change_price(4000)
#
# 而不是：
#
# product1.price = 4000


# ============================================================
# 12. 一句话记忆
# ============================================================

# Encapsulation（封装）：
#
# 把重要资料放在 Class 内部，
# 通过 Method 控制资料如何被访问和修改。
