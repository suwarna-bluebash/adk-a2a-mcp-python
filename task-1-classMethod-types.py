    # Create a class Product with:
    # instance variables: name, price
    # instance method: show_info() → prints product name & price
    # class method: set_discount_rate(rate) → sets a class-level discount
    # static method: is_expensive(price) → returns True if price > 1000

#File_name = task-1-classMethod-types.py


class Product:
    all_products = []  # Class-level list to hold all product instances
    discount_rate = 0  # Class-level discount value

    def __init__(self, name, price):
        self.product_name = name
        self.product_price = price
        Product.all_products.append(self)

    def show_info(self):  
        print(f"Purchased product name is {self.product_name} and the product price is ₹{self.product_price}. Happy Shopping !!!")

    @classmethod
    def set_discount_rate(cls, discount):  
        cls.discount_rate = discount
        for p in cls.all_products:
            p.product_price -= discount
        print(f"Prices after discount:")
        for p in cls.all_products:
            print(f"{p.product_name}: ₹{p.product_price}")

    @staticmethod
    def is_expensive(price):  # Static method
        return price > 1000


p1 = Product("Smart Phone", 50000)
p2 = Product("Book", 500)

p1.show_info()
p2.show_info()

# Apply a discount
Product.set_discount_rate(1000)

# Check if something is expensive and no object needed as static method is there.
print("Is 1500 expensive?", Product.is_expensive(1500))  # True
print("Is 800 expensive?", Product.is_expensive(800))    # False
