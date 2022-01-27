class Items:
    def __init__(self, name, price, type):
        self.name = name
        self.price = price
        self.type = type

    def buy(self):
        print(f"Add {self.name} to list")

    def remove(self):
        print(f"Remove {self.name} from list")


class Cat:
    def __init__(self, name, color, type):
        self.name = name
        self.color = color
        self.type = type

    def feed(self):
        print(f"Successful feeding the {self.name}")


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
    Employee(name="Emi Fukada", position="Waiter", salary="12000"),
    Employee(name="Sora Aoi", position="Chief", salary="21000"),
    Employee(name="Moei Amasuka", position="Cashier", salary="12000"),
    Employee(name="Momonoki Kana", position="Cat sitter", salary="15000"),
]
