class Shelf:
    def __init__(self, name, size) -> None:
        self.name = name
        self.size = size
        self.shelf_list = {}

    def add_to_shelf(self, product, quantity):
        total_qty = 0
        for info in self.shelf_list.values():
            total_qty += info['quantity']

        if total_qty + quantity > self.size:
                print(f"The shelf for {self.name} is full")
        else:
            if product in self.shelf_list:
                self.shelf_list[product]['quantity'] += quantity
            else:
                self.shelf_list[product] = {'quantity': quantity, 'price': product.price}
            print(f"{product.name} is added to {self.name}")

    def remove_to_shelf(self, product, quantity):
        if product in self.shelf_list:
            self.shelf_list[product]['quantity'] -= quantity
            if self.shelf_list[product]['quantity'] <= 0:
                del self.shelf_list[product]
        else:
            print(f"{product.name} is not on {self.name}")

    def display_content(self):
        if not self.shelf_list:
            print(f'\n[{self.name}]\nEmpty Shelf!')
        else:
            available_products = []
            for product, info in self.shelf_list.items():
                available_products.append(f"{product.name} ({info['quantity']} available) | {info['price']:.2f}")
            print(f"\n[{self.name}]")
            for prod_info in available_products:
                print(prod_info)

class Store:
    def __init__(self, name, address) -> None:
        self.name = name
        self.address = address
        self.list_of_shelve = []

    def add_shelve(self, shelf):
        self.list_of_shelve.append(shelf)
        
class Product:
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price

class Cart:
    def __init__(self, size) -> None:
        self.size = size
        self.cart_list = {}

    def display_content(self):
        if len(self.cart_list) == 0:
            print('Your cart is empty!')
        else:
            all_prod = []
            for product, info in self.cart_list.items():
                current_price = info['price']
                updated_price = current_price * info['quantity']
                all_prod.append(f"{product.name:<20}{info['quantity']:<10}{updated_price:<5}")
            print("\n[YOUR CART]")
            print(f"{'NAME':<20}{'QTY':<10}{'PRICE':<5}")
            for prod_info in all_prod:
                print(prod_info)
            print()
            
class Customer:
    def __init__(self, id, name, cart: Cart, budget) -> None:
        self.id = id
        self.name = name
        self.cart = cart
        self.budget = budget
        
    def add_to_cart(self, product, quantity):
        if len(self.cart.cart_list) == self.cart.size:
            print('Your Cart is full')
        else:
            if product in self.cart.cart_list:
                self.cart.cart_list[product]['quantity'] += quantity
            else:
                self.cart.cart_list[product] = {'quantity': quantity, 'price': product.price}
            print(f"{quantity} {product.name} added to your cart")
            for shelf in store.list_of_shelve:
                if product in shelf.shelf_list:
                    if shelf.shelf_list[product]['quantity'] >= quantity:
                        shelf.shelf_list[product]['quantity'] -= quantity
                    else:
                        break
             
    def remove_to_cart(self, product, quantity):
        if product in self.cart.cart_list:
            self.cart.cart_list[product]['quantity'] -= quantity
            print(f"{quantity} {product.name} is remove form the cart")

    def payment(self, subtotal):
        if self.budget < subtotal:
            print('Insufficient Money')
            return False
        else:
            change = self.budget - subtotal
            print(f"Payment Successfull, your change is {change:.2f}")
            return change

class Cashier:
    def __init__(self, name) -> None:
        self.name = name
        self.subtotal = 0

    def calculate_subtotal(self, cart):
        self.subtotal = 0
        for product, info in cart.cart_list.items():
            product_price = info['price']
            product_qty = info['quantity']
            product_total = product_price * product_qty
            self.subtotal += product_total
        print(f"Your total is {self.subtotal}")            
        return self.subtotal
    
    def show_receipt(self, cart, change):
        if cart.cart_list:
            all_prod = []
            total = 0
            for product, info in cart.cart_list.items():
                product_name = product.name
                product_qty = info['quantity']
                product_price = info['price']
                updated_price = product_price * product_qty
                all_prod.append(f"{product_name:<20}{product_qty:<10}{updated_price:<5}")
                total += updated_price
            print("\n[INVOICE RECEIPT]")
            print(f"{'NAME':<20}{'QTY':<10}{'PRICE':<5}")
            for prod_info in all_prod:
                print(prod_info)
            print('--------------------------------------')
            print(f"{'TOTAL':<30}{total:<5}")
            print(f"{'CHANGE':<30}{change}")
            print('Thank you for visiting!')
        else:
            print('Thank you for visiting!')


if __name__ == '__main__':
    # Make the store
    store = Store('Sari Sari Store', 'Pandi')

    # Make shelves
    shelve_1 = Shelf('Mlik', 10)
    shelve_2 = Shelf('Coffee', 10)

    # Add shelves to the store
    store.add_shelve(shelve_1)
    store.add_shelve(shelve_2)

    # Make products
    bear_brand = Product('Bear Brand', 20.00)
    birtch_tree = Product('Birtch Tree', 20.00)
    ensure_gold = Product('Ensure Gold', 30.00)
    great_taste = Product('Great Taste', 12.00)
    nescafe = Product('Nescafe', 12.00)

    # Add products to the shelf
    shelve_1.add_to_shelf(bear_brand, 5)
    shelve_1.add_to_shelf(birtch_tree, 5)
    shelve_1.add_to_shelf(ensure_gold, 5)
    shelve_2.add_to_shelf(great_taste, 5)
    shelve_2.add_to_shelf(nescafe, 5)

    # Dsiplay products of shelves
    shelve_1.display_content()
    shelve_2.display_content()

    # Make cart
    cart = Cart(10)
    
    # MAke cashier
    cashier = Cashier('Jomarie')

    # Make customer
    Mike = Customer('0001', 'Mike', cart, 100)

    # Start Shopping
    Mike.add_to_cart(bear_brand, 2)
    Mike.add_to_cart(great_taste, 3)
    cart.display_content()

    # Dsiplay products of shelves after adding to cart
    shelve_1.display_content()
    shelve_2.display_content()

    # Payment
    cost = cashier.calculate_subtotal(cart)
    change = Mike.payment(cost)
    if change:
        cashier.show_receipt(cart, change)