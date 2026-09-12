# Python OOP - Inventory Management System Notes

========================================
1. OOP 基础
========================================

Class
- Class 是建立 Object 的模板 / 蓝图。

Object
- Object 是 Class 创建出来的实际资料。

Example:
    product1 = Product("Apple", 3.5, 20)

这里：
- Product = Class
- product1 = Object


========================================
2. __init__ 和 self
========================================

__init__
- 创建 Object 时自动执行。
- 用来初始化 Object 的资料。

self
- 代表当前这个 Object。

Example:
    class Product:
        def __init__(self, name, price, stock):
            self.name = name
            self.__price = price
            self.__stock = stock


========================================
3. Attribute 和 Method
========================================

Attribute
- Object 储存的资料。
- 不需要 ()。

Example:
    self.name
    self.__price
    self.__stock

Method
- Object 可以执行的功能。
- 调用时通常需要 ()。

Example:
    product.change_price(100)
    product.add_stock(5)
    product.get_price()


========================================
4. Encapsulation 封装
========================================

使用 __ 可以把 Attribute 做成 private-like。

Example:
    self.__price
    self.__stock

目的：
- 不希望外部直接修改重要资料。
- 让修改资料必须经过 Method。
- 可以在 Method 里面进行 Validation。

Example:
    def change_price(self, price):
        if price <= 0:
            return False

        self.__price = price
        return True


========================================
5. Getter
========================================

Getter 用来读取 private Attribute。

Example:
    def get_price(self):
        return self.__price

    def get_stock(self):
        return self.__stock

Attribute 不需要 ()：
    self.__price

Method 需要 ()：
    self.get_price()


========================================
6. __str__
========================================

__str__ 用来决定 Object 被 print 时显示什么。

Example:
    def __str__(self):
        return (f"Name: {self.name}\n"
                f"   Price : RM{self.__price:.2f}\n"
                f"   Stock: {self.__stock}")

所以：
    print(product1)

Python 会自动调用：
    product1.__str__()


========================================
7. return True / False
========================================

Method 可以使用 True / False 告诉外部操作是否成功。

Example:
    def add_stock(self, qty):
        if qty < 1:
            return False

        self.__stock += qty
        return True

外部可以：
    if product.add_stock(5):
        print("Success")


return 的另一个重要作用：
- 立即结束整个 Method。
- 同时可以把 Value 交出去。


========================================
8. Product Class
========================================

Product 负责管理自己的资料和规则。

主要 Attribute:
    name
    __price
    __stock

主要 Method:
    __str__()
    to_dict()
    change_price()
    add_stock()
    remove_stock()
    sell()
    get_price()
    get_stock()


========================================
9. Inventory Class
========================================

Inventory 负责管理很多 Product Objects。

Example:
    class Inventory:
        def __init__(self):
            self.products = []

所以：

    inventory.products

是一个 List，里面放 Product Objects。


========================================
10. Object 之间的调用
========================================

Inventory 可以找到 Product，然后调用 Product 的 Method。

Example:
    for product in self.products:
        if name == product.name:
            return product.add_stock(stock)

这里：
- Inventory 找到 Product
- Product 自己负责修改 stock
- Product 返回 True / False
- Inventory 把结果 return 出去


这种设计可以让：
- Product 管理自己的资料
- Inventory 管理 Product


========================================
11. CRUD
========================================

CRUD:

Create
- add_product()

Read
- view_products()
- search_product()

Update
- edit_product_price()
- add_stock()
- remove_stock()

Delete
- delete_product()


========================================
12. enumerate()
========================================

enumerate() 可以同时取得：
- index
- value

Example:
    for index, product in enumerate(self.products):
        print(f"{index + 1}. {product}")

index 从 0 开始。

所以：
    index + 1

可以让用户看到：
    1.
    2.
    3.


========================================
13. to_dict()
========================================

JSON 不能直接储存自己的 Product Object。

所以 Product 需要转换成 Dictionary。

Example:
    def to_dict(self):
        return {
            "name": self.name,
            "price": self.get_price(),
            "stock": self.get_stock()
        }

流程：

Product Object
    ↓
Dictionary


========================================
14. to_list()
========================================

Inventory 里面有很多 Product Objects。

所以需要把每一个 Product 转成 Dictionary。

Example:
    def to_list(self):
        products_list = []

        for product in self.products:
            item = product.to_dict()
            products_list.append(item)

        return products_list

流程：

Product Object
    ↓
to_dict()
    ↓
Dictionary
    ↓
products_list


注意：

return 要放在 for 外面。

错误：
    for product in self.products:
        ...
        return products_list

这样只会处理第一个 Product。

正确：
    for product in self.products:
        ...

    return products_list

这样会先处理全部 Product，最后才 return。


========================================
15. JSON 基础
========================================

dump
- Python → JSON File

load
- JSON File → Python

dumps
- Python → JSON String

loads
- JSON String → Python


最常用：

    json.dump()
    json.load()


========================================
16. Save JSON
========================================

Save 的流程：

Python Objects
    ↓
to_dict()
    ↓
Dictionary
    ↓
to_list()
    ↓
List of Dictionaries
    ↓
json.dump()
    ↓
JSON File


Example:

    def save_json(self):
        path_file = r"C:\Users\user\Desktop\workshop\oop.inventory.json"
        product_list = self.to_list()

        with open(path_file, "w", encoding="utf8") as file:
            json.dump(
                product_list,
                file,
                indent=4,
                ensure_ascii=False
            )


为什么：
    self.to_list()

而不是：
    self.to_list

因为 to_list 是 Method。

    self.to_list
    = Method 本身

    self.to_list()
    = 执行 Method


========================================
17. Load JSON
========================================

Load 的流程刚好相反：

JSON File
    ↓
json.load()
    ↓
List of Dictionaries
    ↓
取出 name / price / stock
    ↓
重新创建 Product Object
    ↓
加入 Inventory


Example:

    def load_json(self):
        path_file = r"C:\Users\user\Desktop\workshop\oop.inventory.json"

        with open(path_file, "r", encoding="utf8") as file:
            products = json.load(file)

        for data in products:
            name = data["name"]
            price = data["price"]
            stock = data["stock"]

            product = Product(name, price, stock)
            self.add_product(product)


重点：

JSON 里面储存的是 Dictionary，
不是 Product Object。

所以 Load 时必须重新：

    Product(name, price, stock)

创建 Product Object。


========================================
18. Save / Load 为什么通常不用 return
========================================

return 的作用之一是：
- 把结果交给其他地方。

例如：

    def to_list(self):
        ...
        return products_list

因为 save_json() 需要拿到这个 List。

但是：

    save_json()

主要工作是：
- 把资料写进文件。

    load_json()

主要工作是：
- 从文件读取资料
- 创建 Product
- 加入 self.products

它们主要是在执行 Action，
所以不需要为了结果而 return。


简单记：

需要把结果交出去
→ return

只是执行一个动作
→ 通常不需要 return


========================================
19. Auto Save
========================================

修改 Inventory 后马上 Save。

Example:

Add Product:
    inventory.add_product(product)
    inventory.save_json()

Delete:
    inventory.delete_product(delete)
    inventory.save_json()

Edit Price:
    inventory.edit_product_price(name, price)
    inventory.save_json()

Add Stock:
    inventory.add_stock(name, stock)
    inventory.save_json()

Remove Stock:
    inventory.remove_stock(name, stock)
    inventory.save_json()


流程：

User 修改资料
    ↓
Inventory 改变
    ↓
save_json()
    ↓
马上写入 JSON


========================================
20. 程序启动时 Load
========================================

程序开始：

    inventory = Inventory()
    inventory.load_json()

这样程序重新启动时，
之前保存的 Product 会重新进入：

    inventory.products


所以：

启动程序
    ↓
load_json()
    ↓
读取 JSON
    ↓
重新创建 Product Objects
    ↓
Inventory


========================================
21. Input Validation
========================================

整数：

    def error_int(prompt):
        while True:
            try:
                value = int(input(prompt))

                if value <= 0:
                    print("Quantity Cant Be Negative")
                else:
                    return value

            except ValueError:
                print("Error")


作用：
- 防止输入不能转换成 int 的资料。
- 防止数量 <= 0。


浮点数：

    def error_float(prompt):
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("Error")


========================================
22. 完整项目资料流
========================================

                USER
                  ↓
                MENU
                  ↓
             INVENTORY
                  ↓
        ┌─────────┴─────────┐
        ↓                   ↓
    Product Objects      JSON File
        ↓                   ↑
   Product Methods      Save / Load
        ↓                   ↑
     self.products ←────────┘


Save：

Product Object
→ to_dict()
→ Dictionary
→ to_list()
→ List
→ json.dump()
→ JSON


Load：

JSON
→ json.load()
→ List of Dictionary
→ Product()
→ self.add_product()
→ Product Objects


========================================
23. 目前项目完成进度
========================================

[✓] Class
[✓] Object
[✓] __init__
[✓] self
[✓] Attribute
[✓] Method
[✓] Method Parameter
[✓] Method 修改 Attribute
[✓] Method 调用 Method
[✓] return
[✓] Encapsulation
[✓] Getter
[✓] __str__
[✓] CRUD
[✓] Inventory Management
[✓] to_dict()
[✓] to_list()
[✓] JSON dump
[✓] JSON load
[✓] Save JSON
[✓] Load JSON
[✓] Auto Save
[✓] Auto Load

下一阶段：
→ Code Refactoring / 代码整理
→ 检查重复代码
→ 改善命名
→ 改善错误处理
→ 让整个 Project 更接近真实项目
