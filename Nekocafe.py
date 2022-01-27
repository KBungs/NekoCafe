class Items:
    def __init__(self, name, price, type):
        self.name = name
        self.price = price
        self.type = type

    def buy(self):
        print(f"Add {self.name} to list")

    def remove(self):
        print(f"Remove {self.name} from list")
        
    def set_price(self, price):
        self.price = price
        print(f"{self.name} set price to {self.price}")
        
    def set_name(self, price):
        self.price = price
        print(f"Success set name to {self.name}")
        


class Cat:
    def __init__(self, name, color, type):
        self.name = name
        self.color = color
        self.type = type

    def feed(self):
        print(f"Successful feeding the {self.name}")
        
    def change_cat_name(self, name):
        self.name = name
        print(f"Success change the cat name to {self.name}")
        
    def change_cat_color(self, color):
        self.color = color
        print(f"Success change the cat color to {self.name}")
        
    def change_cat_type(self, type):
        self.type = type
        print(f"Success change the cat type to {self.name}")


class Employee:
    def __init__(self, id, name, position, salary):
        self.id = id
        self.name = name
        self.position = position
        self.salary = salary

    def paid(self):
        print(f"Successful paid salary {self.salary} to {self.name}")
        
    def fire(self):
        print(f"Successful fire {self.name}")
        
    def set_id(self, id):
        self.id = id
        print(f"{self.name} set id to {self.id}")
        
    def set_name(self, name):
        self.name = name
        print(f"set new name to {self.name}")
        
    def set_salary(self, salary):
        self.salary = salary
        print(f"set salary to {self.salary}")
        
    def set_position(self, position):
        self.position = position
        print(f"set salary to {self.salary}")


cats = [
    Cat(
        name="Nami",
        color="White",
        type="Ragdoll"
    ),

    Cat(
        name="Boa",
        color="White",
        type="Persian"
    ),

    Cat(
        name="Shiro",
        color="Black",
        type="Maine Coon"
    ),

    Cat(
        name="Salmon",
        color="Orange",
        type="Siam"
    )

]
menu = [
    Items(name="Brownie", price="50", type="Dessert"),
    Items(name="Craissant", price="22", type="Dessert"),
    Items(name="Cake", price="45", type="Dessert"),

    Items(name="Water", price="10", type="Drinks"),
    Items(name="Latte", price="65", type="Drinks"),
    Items(name="Americano", price="40", type="Drinks"),
    Items(name="Espeso", price="40", type="Drinks"),
    Items(name="Italian Soda", price="50", type="Drinks")
]

employees = [
    Employee(name="Sky Kung", position="Manager", salary="25000"),
    Employee(name="Emi Fukada", position="Waiter", salary="12000"),
    Employee(name="Sora Aoi", position="Chief", salary="21000"),
    Employee(name="Moei Amasuka", position="Cashier", salary="12000"),
    Employee(name="Momonoki Kana", position="Cat sitter", salary="15000"),
]
