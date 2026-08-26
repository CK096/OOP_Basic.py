对！👏 你前面的理解完全正确，而且你现在刚好碰到了 Inheritance 的下一个核心问题：

Parent 的 Method 可以被 Child 继承，但 Parent 不知道 Child 特有的 Attribute。

你这份代码本身写得很好。

① 为什么 add_stock() 可以用？

你说的：

add_stock() 可以用是因为它是在 Parent Class 里面的

完全正确。 ✅

结构是：

Product
├── display()
└── add_stock()
       ↑
       │ 继承
       │
┌──────┴─────────┐
FoodProduct   ElectronicProduct

所以：

food1.add_stock(5)

Python 会找：

FoodProduct
↓
有没有 add_stock()？
↓
没有
↓
去 Parent Product 找
↓
找到！
↓
执行 Product.add_stock()

所以可以正常使用。

② 那为什么 display() 没有 Expired / Warranty？

因为你的 display() 是 Parent 的：

def display(self):
    print(f"Name: {self.name}")
    print(f"Price : RM {self.price:.2f}")
    print(f"Stock : {self.stock}")

它只知道：

Product 有：
name
price
stock

它不知道：

FoodProduct 才有：
expired_date

ElectronicProduct 才有：
warranty

所以：

food1.display()

实际上调用的是：

FoodProduct
↓
没有 display()
↓
Product.display()

而 Product.display() 只打印：

Name
Price
Stock
③ 你的理解「不能把它加入 Parent」也是对的

你说：

又不能加入 Parent Class 里面

对。

如果你写：

class Product:
    def display(self):
        print(self.name)
        print(self.price)
        print(self.stock)
        print(self.expired_date)
        print(self.warranty)

就会很奇怪。

因为普通的：

Product

根本没有：

expired_date
warranty

例如：

product1 = Product("Book", 20, 10)
product1.display()

Python 找不到：

self.expired_date

就会报：

AttributeError

所以你不能把 Child 特有的东西硬塞进 Parent。

🔥 这就是为什么 Child 可以 Override Method

这里就是 Inheritance 的下一个重要概念：

Method Overriding（方法覆盖 / 重写）

我们可以让 FoodProduct 自己重新写一个 display()。

class FoodProduct(Product):
    def __init__(self, name, price, stock, expired_date):
        super().__init__(name, price, stock)
        self.expired_date = expired_date

    def display(self):
        print(f"Name: {self.name}")
        print(f"Price : RM {self.price:.2f}")
        print(f"Stock : {self.stock}")
        print(f"Expired Date : {self.expired_date}")

现在：

food1.display()

Python 会：

FoodProduct
↓
找到 display()
↓
直接执行 FoodProduct.display()

而不是去 Parent。

结果：

Name: Apple
Price : RM 3.50
Stock : 25
Expired Date : 02/09/2026
④ ElectronicProduct 也是一样
class ElectronicProduct(Product):
    def __init__(self, name, price, stock, warranty):
        super().__init__(name, price, stock)
        self.warranty = warranty

    def display(self):
        print(f"Name: {self.name}")
        print(f"Price : RM {self.price:.2f}")
        print(f"Stock : {self.stock}")
        print(f"Warranty : {self.warranty} months")

所以：

electronic1.display()

会用：

ElectronicProduct.display()

而不是：

Product.display()
🧠 现在出现一个很重要的结构

你现在看到：

Product
│
├── display()
├── add_stock()
│
├── FoodProduct
│   ├── set_expired_date()
│   └── display() ← 覆盖 Parent
│
└── ElectronicProduct
    ├── set_warranty()
    └── display() ← 覆盖 Parent

这就是：

Method Overriding

Child 可以：

继承 Parent 的 Method，也可以自己重新定义同名 Method。

⭐ 但是这里又出现一个新问题

你会发现：

Food：

def display(self):
    print(f"Name: {self.name}")
    print(f"Price : RM {self.price:.2f}")
    print(f"Stock : {self.stock}")
    print(f"Expired Date : {self.expired_date}")

Electronic：

def display(self):
    print(f"Name: {self.name}")
    print(f"Price : RM {self.price:.2f}")
    print(f"Stock : {self.stock}")
    print(f"Warranty : {self.warranty}")

你又开始重复：

print(name)
print(price)
print(stock)

😆

而这正好带我们进入：

super().display()

我们可以让 Child：

def display(self):
    super().display()
    print(f"Expired Date : {self.expired_date}")

意思：

FoodProduct.display()
       ↓
super().display()
       ↓
Product.display()
       ↓
显示 Name / Price / Stock
       ↓
回到 FoodProduct
       ↓
显示 Expired Date

这样就不用重复写 Parent 的代码。

你现在已经碰到 Inheritance 的三个核心：
① Inheritance
Child 可以继承 Parent 的 Attribute / Method

② Method Overriding
Child 可以重新定义 Parent 已经有的 Method

③ super()
Child 可以调用 Parent 的 Method

你刚才自己发现的：

“display 不能直接放 Expired / Warranty 到 Parent，因为 Parent 根本没有这些资料。”

这个理解非常重要。

下一步我们就专门练 super().display()，然后再进入 Polymorphism（多态）。

def display(self):
    print(f"Name: {self.name}\n"
          f"Price : RM {self.price:.2f}\n"
          f"Stock : {self.stock}\n"
          f"Expired Date: {self.expired_date}")

super()在__init__的时候需要重复写一次，可是在display()的时候就不需要重写了

对，你的理解已经很接近了，不过有一个地方要修正：

super() 不是因为 __init__ 才需要，而是看你有没有需要使用 Parent 的东西。

① __init__ 为什么通常要 super()？

例如：

class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

Child：

class FoodProduct(Product):
    def __init__(self, name, price, stock, expired_date):
        super().__init__(name, price, stock)
        self.expired_date = expired_date

这里需要：

super().__init__(name, price, stock)

因为我们不想重新写：

self.name = name
self.price = price
self.stock = stock

所以：

super().__init__()
        ↓
交给 Product.__init__()
        ↓
建立 name / price / stock
② display() 其实也可以使用 super()

你现在写：

def display(self):
    print(f"Name: {self.name}\n"
          f"Price : RM {self.price:.2f}\n"
          f"Stock : {self.stock}\n"
          f"Expired Date: {self.expired_date}")

可以用，而且完全正确。

但是这样你把 Parent 的：

Name
Price
Stock

全部重新写了一次。

其实可以：

def display(self):
    super().display()
    print(f"Expired Date: {self.expired_date}")

这样就不用重复写 Parent 的代码。

③ 所以 super() 在两个地方的作用其实很像
__init__
super().__init__(name, price, stock)

意思：

使用 Parent 的初始化逻辑。

display()
super().display()

意思：

使用 Parent 的 display()。

🧠 所以不要记成：

__init__ 要 super()，display() 不需要。

应该记成：

Child 如果需要使用 Parent 的 Method，可以用 super() 调用。

例如：
class FoodProduct(Product):

    def __init__(self, name, price, stock, expired_date):
        super().__init__(name, price, stock)
        self.expired_date = expired_date

    def display(self):
        super().display()
        print(f"Expired Date: {self.expired_date}")

    def set_expired_date(self, date):
        self.expired_date = date

整个流程：

FoodProduct
│
├── __init__()
│     ↓
│   super().__init__()
│     ↓
│   Product.__init__()
│
├── display()
│     ↓
│   super().display()
│     ↓
│   Product.display()
│
└── set_expired_date()
      ↓
    FoodProduct 自己处理
⭐ 最重要的一句话
super()
↓
调用 Parent 的东西

不管那个东西是：

__init__()

还是：

display()

甚至以后可以是：

其他 Method

都可以用 super()。

你现在已经把 Inheritance + super() + Method Overriding 串起来了。下一步就是很有意思的 Polymorphism（多态）。

Today 3:45 PM
class Product:
    def __init__(self,name,price,stock):
        self.name = name
        self.price = price
        self.stock = stock

    def display(self):
        print(f"Name: {self.name}\n"
              f"Price : RM {self.price:.2f}\n"
              f"Stock : {self.stock}")

    def add_stock(self,qty):
        if qty < 1:
            print("Add Stock Minimum need 1")
        else:
            self.stock += qty
            print(f"Add {self.name} {qty} Stock Complete")

class FoodProduct(Product):
    def __init__(self,name,price,stock,expired_date):
        super().__init__(name,price,stock)
        self.expired_date = expired_date

    def set_expired_date(self,date):
        self.expired_date = date

    def display(self):
        print(f"Name: {self.name}\n"
              f"Price : RM {self.price:.2f}\n"
              f"Stock : {self.stock}\n"
              f"Expired Date: {self.expired_date}")

class ElectronicProduct(Product):
    def __init__(self,name,price,stock,warranty):
        super().__init__(name,price,stock)
        self.warranty = warranty

    def set_warranty(self,warranty):
        self.warranty = warranty

    def display(self):
        super().display()
        print(f"Warranty : {self.warranty} Month")


food1 = FoodProduct("Apple",3.50,20,"31/08/2026")
food1.add_stock(5)
food1.set_expired_date("02/09/2026")
food1.display()

electronic1 = ElectronicProduct("Laptop",3500,5,24)
electronic1.add_stock(3)
electronic1.set_warranty(36)
electronic1.display()

可以帮我注释Super() + inheritace 吗，我要记录在github

当然可以。你这份代码已经很适合拿来当 Inheritance + super() 的练习笔记了。我帮你保留原本的代码风格，只加入重点注释，方便你直接放 GitHub。

# ============================================================
# OOP - Inheritance（继承）
# ============================================================

# Inheritance = 继承
#
# Child Class 可以继承 Parent Class 的：
# - Attribute
# - Method
#
# 这样可以避免重复写相同的代码。
#
#
# Parent Class
#      ↓
#    Product
#      ↓
# ┌────┴──────────────┐
# ↓                   ↓
# FoodProduct    ElectronicProduct
#
#
# Product = Parent Class（父类）
# FoodProduct / ElectronicProduct = Child Class（子类）


# ============================================================
# 1. Parent Class
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
# 2. Child Class - FoodProduct
# ============================================================

# class FoodProduct(Product)
#
# Product 放在括号里面
# 代表 FoodProduct 继承 Product。
#
# FoodProduct 可以直接使用 Product 的：
#
# Attribute：
# name
# price
# stock
#
# Method：
# display()
# add_stock()


class FoodProduct(Product):

    def __init__(self, name, price, stock, expired_date):

        # super()
        #
        # super() = 调用 Parent Class 的东西
        #
        # super().__init__()
        # = 调用 Parent Class 的 __init__()
        #
        # 所以这里会执行：
        #
        # Product.__init__(name, price, stock)
        #
        # 帮我们建立：
        # self.name
        # self.price
        # self.stock

        super().__init__(name, price, stock)

        # 下面是 FoodProduct 自己特有的 Attribute
        self.expired_date = expired_date

    def set_expired_date(self, date):
        # FoodProduct 自己的 Method
        self.expired_date = date

    def display(self):

        # Child 可以重新定义 Parent 已经存在的 Method。
        #
        # 这叫：
        # Method Overriding（方法重写）
        #
        # 这里我们没有使用 super().display()
        # 而是把 Parent 的 display 内容重新写一次，
        # 再加入 FoodProduct 自己的 expired_date。

        print(f"Name: {self.name}\n"
              f"Price : RM {self.price:.2f}\n"
              f"Stock : {self.stock}\n"
              f"Expired Date: {self.expired_date}")


# ============================================================
# 3. Child Class - ElectronicProduct
# ============================================================

class ElectronicProduct(Product):

    def __init__(self, name, price, stock, warranty):

        # 调用 Parent Class 的 __init__()
        #
        # Product 会负责建立：
        # name
        # price
        # stock

        super().__init__(name, price, stock)

        # ElectronicProduct 自己特有的 Attribute
        self.warranty = warranty

    def set_warranty(self, warranty):
        # ElectronicProduct 自己的 Method
        self.warranty = warranty

    def display(self):

        # super().display()
        #
        # 调用 Parent Class 的 display()
        #
        # 先让 Product.display() 负责：
        # Name
        # Price
        # Stock
        #
        # 然后回到这里，
        # 再显示 ElectronicProduct 自己的 warranty。

        super().display()

        print(f"Warranty : {self.warranty} Month")


# ============================================================
# 4. 使用 FoodProduct
# ============================================================

food1 = FoodProduct(
    "Apple",
    3.50,
    20,
    "31/08/2026"
)

# add_stock() 没有写在 FoodProduct
# 但是 FoodProduct 继承了 Product，
# 所以可以直接使用 Parent 的 add_stock()。

food1.add_stock(5)

# 使用 FoodProduct 自己的 Method
food1.set_expired_date("02/09/2026")

# FoodProduct 自己重新定义了 display()
# 所以这里会使用 FoodProduct.display()

food1.display()


# ============================================================
# 5. 使用 ElectronicProduct
# ============================================================

electronic1 = ElectronicProduct(
    "Laptop",
    3500,
    5,
    24
)

# add_stock() 来自 Parent Class Product
# ElectronicProduct 继承了它，所以可以直接使用。

electronic1.add_stock(3)

# ElectronicProduct 自己的 Method
electronic1.set_warranty(36)

# ElectronicProduct 有自己的 display()
#
# display() 内部：
#
# super().display()
#       ↓
# Product.display()
#       ↓
# 显示 Name / Price / Stock
#       ↓
# 回到 ElectronicProduct.display()
#       ↓
# 显示 Warranty

electronic1.display()


# ============================================================
# 6. Inheritance 的重点
# ============================================================

# Parent Class：
#
# Product
# ├── name
# ├── price
# ├── stock
# ├── display()
# └── add_stock()
#
#
# Child Class：
#
# FoodProduct
# ├── 继承 name
# ├── 继承 price
# ├── 继承 stock
# ├── 继承 add_stock()
# ├── expired_date
# └── set_expired_date()
#
#
# ElectronicProduct
# ├── 继承 name
# ├── 继承 price
# ├── 继承 stock
# ├── 继承 add_stock()
# ├── warranty
# └── set_warranty()


# ============================================================
# 7. super() 的重点
# ============================================================

# super() = 使用 Parent Class 的东西
#
#
# 在 __init__：
#
# super().__init__(name, price, stock)
#
# = 调用 Parent 的 __init__()
#
#
# 在其他 Method：
#
# super().display()
#
# = 调用 Parent 的 display()
#
#
# 所以不要记成：
#
# "__init__ 一定要用 super()"
#
# 而是：
#
# "如果 Child 需要使用 Parent 的 Method，
#  可以使用 super() 来调用。"


# ============================================================
# 8. Method Overriding（方法重写）
# ============================================================

# Parent 有：
#
# def display(self):
#     ...
#
#
# Child 也可以重新写：
#
# def display(self):
#     ...
#
#
# 当执行：
#
# food1.display()
#
# Python 会优先寻找 FoodProduct 有没有 display()
#
# 有：
# ↓
# 使用 FoodProduct.display()
#
#
# 如果 Child 没有 display()
# ↓
# 去 Parent Product 找
# ↓
# 使用 Product.display()


# ============================================================
# 9. super().display() 和直接重写的区别
# ============================================================

# 方法 1：全部重新写
#
# def display(self):
#     print(self.name)
#     print(self.price)
#     print(self.stock)
#     print(self.expired_date)
#
# 缺点：
# Parent 的代码重复写了一次。


# 方法 2：使用 super()
#
# def display(self):
#     super().display()
#     print(self.expired_date)
#
# 优点：
# 直接使用 Parent 已经写好的 display()
# 然后只增加 Child 自己的内容。


# ============================================================
# 10. 一句话记忆
# ============================================================

# Inheritance：
#
# Child Class 可以继承 Parent Class 的 Attribute 和 Method。
#
#
# super()：
#
# 用来调用 Parent Class 的 Method。
#
#
# Method Overriding：
#
# Child 可以重新定义 Parent 已经存在的 Method。
#
#
# 最重要的结构：
#
# Parent
#    ↓
# Child
#    ↓
# 继承 + 增加自己的功能

你这份现在已经可以作为 OOP → Inheritance 的 GitHub 笔记了。

目前你的 OOP 路线已经到：

Class
Object
__init__
self
Attribute
Method
Method 参数
Method 修改 Attribute
Method 调用 Method
return
__str__
Encapsulation
        ↓
Inheritance        ← 现在
super()
Method Overriding
        ↓
Polymorphism       ← 下一步

而且你刚刚已经自己发现了一个很重要的区别：super().__init__() 是调用 Parent 的初始化，而 super().display() 是调用 Parent 的 Method。这个理解比单纯记语法重要很多。
