# ============================================================
# OOP - Polymorphism（多态）
# ============================================================

# Polymorphism = 多态
#
# 简单来说：
#
# 相同的 Method
#       ↓
# 不同的 Object
#       ↓
# 可以执行不同的行为
#
#
# 例如：
#
# food1.display()
# electronic1.display()
# cloth1.display()
#
# 虽然都是 display()
# 但是每个 Object 会执行自己 Class 的 display()。


# ============================================================
# 1. Polymorphism 的基本概念
# ============================================================

# Parent Class：
#
# Product
#
# Child Class：
#
# FoodProduct
# ElectronicProduct
# ClothingProduct
#
#
# 三个 Child 都可以有自己的：
#
# display()
#
#
# 当调用：
#
# product.display()
#
# Python 会根据 Object 实际属于哪个 Class，
# 决定执行哪个 display()。


# ============================================================
# 2. Parent Class
# ============================================================

class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def display(self):
        print(f"Name: {self.name}\n"
              f"Price : RM {self.price:.2f}\n"
              f"Stock : {self.stock}")

    def add_stock(self, qty):
        if qty < 1:
            print("Add Stock Minimum need 1")
        else:
            self.stock += qty
            print(f"Add {self.name} {qty} Stock Complete")


# ============================================================
# 3. FoodProduct
# ============================================================

class FoodProduct(Product):

    def __init__(self, name, price, stock, expired_date):

        # 调用 Parent Class 的 __init__()
        super().__init__(name, price, stock)

        # FoodProduct 自己的 Attribute
        self.expired_date = expired_date

    def set_expired_date(self, date):
        self.expired_date = date

    def display(self):

        # 使用 Parent 的 display()
        super().display()

        # 加上 FoodProduct 自己的资料
        print(f"Expired Date: {self.expired_date}")


# ============================================================
# 4. ElectronicProduct
# ============================================================

class ElectronicProduct(Product):

    def __init__(self, name, price, stock, warranty):

        # 调用 Parent Class 的 __init__()
        super().__init__(name, price, stock)

        # ElectronicProduct 自己的 Attribute
        self.warranty = warranty

    def set_warranty(self, warranty):
        self.warranty = warranty

    def display():

        # 调用 Parent 的 display()
        super().display()

        # 加上 ElectronicProduct 自己的资料
        print(f"Warranty : {self.warranty} Month")


# ============================================================
# 5. ClothingProduct
# ============================================================

class ClothingProduct(Product):

    def __init__(self, name, price, stock, size):

        # 调用 Parent Class 的 __init__()
        super().__init__(name, price, stock)

        # ClothingProduct 自己的 Attribute
        self.size = size

    def cloth_size(self, size):
        size = size.lower()
        if size not in ("s", "m", "l"):
            print("Incorrect Size")
        else:
            self.size = size.upper()

    def display():

        # 调用 Parent 的 display()
        super().display()

        # 加上 ClothingProduct 自己的资料
        print(f"Size : {self.size}")


# ============================================================
# 6. 建立不同的 Object
# ============================================================

food1 = FoodProduct("Apple",3.50,20,"31/08/2026")

electronic1 = ElectronicProduct("Laptop",3500,5,24)

cloth1 = ClothingProduct("Red",35,200,"L")


# ============================================================
# 7. 不同 Object 有自己的 display()
# ============================================================

food1.display()

# FoodProduct.display()
#
# 输出：
#
# Name
# Price
# Stock
# Expired Date


electronic1.display()

# ElectronicProduct.display()
#
# 输出：
#
# Name
# Price
# Stock
# Warranty


cloth1.display()

# ClothingProduct.display()
#
# 输出：
#
# Name
# Price
# Stock
# Size


# ============================================================
# 8. Polymorphism 的关键
# ============================================================

products = [
    food1,
    electronic1,
    cloth1
]


for product in products:
    product.display()


# 这里没有写：
#
# if product 是 FoodProduct:
#     ...
#
# elif product 是 ElectronicProduct:
#     ...
#
# elif product 是 ClothingProduct:
#     ...
#
#
# 只需要：
#
# product.display()
#
#
# Python 会自动根据 Object 的 Class
# 找到对应的 display()。


# ============================================================
# 9. for Loop 实际发生什么？
# ============================================================

# 第一次：
#
# product = food1
#
# food1 属于 FoodProduct
#
#       ↓
#
# FoodProduct.display()

# 第二次：
#
# product = electronic1
#
# electronic1 属于 ElectronicProduct
#
#       ↓
#
# ElectronicProduct.display()

# 第三次：
#
# product = cloth1
#
# cloth1 属于 ClothingProduct
#
#       ↓
#
# ClothingProduct.display()


# ============================================================
# 10. Polymorphism 的结构
# ============================================================

#                 Product
#                    │
#          ┌─────────┼─────────┐
#          ↓         ↓         ↓
#     FoodProduct  Electronic  Clothing
#          │         Product    Product
#          │           │          │
#          ↓           ↓          ↓
#      display()   display()  display()
#          │           │          │
#          └───────────┼──────────┘
#                      ↓
#               for product
#                      ↓
#               product.display()
#                      ↓
#              不同 Object
#              不同行为


# ============================================================
# 11. Method Overriding + Polymorphism
# ============================================================

# Polymorphism 通常会和 Method Overriding 一起出现。
#
#
# Parent：
#
# def display(self):
#     ...
#
#
# Child：
#
# def display(self):
#     ...
#
#
# Child 重新定义 Parent 已经存在的 Method，
# 叫做：
#
# Method Overriding（方法重写）
#
#
# 然后不同 Child Object 调用同一个 Method 名称，
# 却执行不同的代码，
# 就形成 Polymorphism。


# ============================================================
# 12. 为什么 Polymorphism 有用？
# ============================================================

# 假设 Inventory 里面有：
#
# 100 个 Product
#
# 里面可能有：
#
# FoodProduct
# ElectronicProduct
# ClothingProduct
# ...
#
#
# 我们不需要知道每个 Product 是什么类型。
#
# 只需要：
#
# for product in products:
#     product.display()
#
#
# 每个 Object 会自动执行自己的 display()。


# ============================================================
# 13. 不使用 Polymorphism
# ============================================================

# 可能会写成：
#
# for product in products:
#
#     if isinstance(product, FoodProduct):
#         product.display()
#
#     elif isinstance(product, ElectronicProduct):
#         product.display()
#
#     elif isinstance(product, ClothingProduct):
#         product.display()
#
#
# 这样代码会越来越长。
#
# 如果以后增加：
#
# FurnitureProduct
#
# 又要增加一个 if。


# ============================================================
# 14. 使用 Polymorphism
# ============================================================

for product in products:
    product.display()


# 简单很多。
#
# 不需要知道：
#
# Product 是什么
# FoodProduct 是什么
# ElectronicProduct 是什么
# ClothingProduct 是什么
#
# 只需要知道：
#
# "这个 Object 有 display()"
#
# 就可以调用。


# ============================================================
# 15. Polymorphism 最重要的概念
# ============================================================

# 相同的 Method
#       ↓
# 不同的 Object
#       ↓
# 不同的行为
#
#
# 例如：
#
# food1.display()
# electronic1.display()
# cloth1.display()
#
# 都是：
#
# display()
#
# 但是执行的内容不同。


# ============================================================
# 16. 一句话记忆
# ============================================================

# Polymorphism（多态）：
#
# "同一个 Method，可以根据不同的 Object，
#  执行不同的行为。"
