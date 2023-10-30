from datetime import datetime as dt

class Soda:
    def __init__(self, id, brand, name, price, exp_date, mfg_date) -> None:
        self.id = id
        self.name = name
        self.brand = brand
        self.price = price
        self.exp_date = exp_date
        self.mfg_date = mfg_date

class Chip:
    def __init__(self, id, brand, name, price, exp_date, mfg_date) -> None:
        self.id = id
        self.name = name
        self.brand = brand
        self.price = price
        self.exp_date = exp_date
        self.mfg_date = mfg_date

class Bread:
    def __init__(self, id, brand, name, price, exp_date, mfg_date) -> None:
        self.id = id
        self.name = name
        self.brand = brand
        self.price = price
        self.exp_date = exp_date
        self.mfg_date = mfg_date

class Milk:
    def __init__(self, id, brand, name, price, exp_date, mfg_date) -> None:
        self.id = id
        self.name = name
        self.brand = brand
        self.price = price
        self.exp_date = exp_date
        self.mfg_date = mfg_date

class Chocolate:
    def __init__(self, id, brand, name, price, exp_date, mfg_date) -> None:
        self.id = id
        self.name = name
        self.brand = brand
        self.price = price
        self.exp_date = exp_date
        self.mfg_date = mfg_date

class Store:
    def __init__(self, name, location) -> None:
        self.name = name
        self.location = location
        self.list_of_products = []
        self.list_of_expired_prod = []

    def display_products(self):
        if len(self.list_of_products) == 0:
            print('No products available')
        else:
            current_date = dt.now()
            formatted_current_date = current_date.strftime("%m/%d/%Y")
            print('[Available Products]')
            for supply in self.list_of_products:
                formatted_exp_date = supply.product.exp_date
                if formatted_current_date > formatted_exp_date:
                    print(f"{supply.product.name} with quantity of {supply.quantity} has been expired!")
                    self.list_of_expired_prod.append(supply)
                    continue
                print(f"Product ID: {supply.product.id}")
                print(f"Product Brand: {supply.product.brand}")
                print(f"Product Name: {supply.product.name}")
                print(f"Product Price: {supply.product.price}")
                print(f"Available Quantity: {supply.quantity}")
                print(f"Expiration Date: {supply.product.exp_date}")
                print('----------------------------------------')

    def display_expired_products(self):
        if len(self.list_of_expired_prod) == 0:
            print('No expired products!')
        else:
            print('[List of Expired Products]')
            for supply in self.list_of_expired_prod:
                product = supply.product
                quantity = supply.quantity
                print(f"Product ID: {product.id}")
                print(f"Product Brand: {product.brand}")
                print(f"Product Name: {product.name}")
                print(f"Product Price: {product.price}")
                print(f"Expired Quantity: {quantity}")
                print(f"Expiration Date: {product.exp_date}")
                print('----------------------------------------')

    def return_product(self, supplier):
        if len(self.list_of_expired_prod) == 0:
            print('Nothing to return to the supplier!')
        else:
            for supply in self.list_of_expired_prod:
                supplier.expired_list.append(supply)
            self.list_of_expired_prod.clear()

class Supply:
    def __init__(self, product, qty) -> None:
        self.product = product
        self.quantity = qty

class Supplier:
    def __init__(self, name, address) -> None:
        self.name = name
        self.address = address
        self.list_of_supplies = []
        self.expired_list = []

    def add_supply(self, product, qty):
        supply = Supply(product, qty)
        self.list_of_supplies.append(supply)
        return supply

    def deliver_supply(self, supply, qty, store):
        if supply.quantity < qty:
            print('Not enough product for delivery')
            return
        else:
            supply.quantity -= qty
            store.list_of_products.append(Supply(supply.product, qty))
            print(f"The {supply.product.name} with quantity of {supply.quantity} have been delivered to the {store.name}")

    def display_list_of_supplies(self):
        if len(self.list_of_supplies) == 0:
            print('No product in the supply list!')
        else:
            print('[List of Supplies]')
            for supply in self.list_of_supplies:
                print(f"Product: {supply.product.name}")
                print(f"Quantity: {supply.quantity}")
                print(f"Exp Date: {supply.product.exp_date}")
                print('----------------------------------------')

if __name__ == '__main__':
    # Make the product
    coke_zero = Soda('00001', 'Coca Cola', 'Coke Zero', 20.00, '09/30/2023', '01/09/2023')
    gardenia = Bread('00001', 'Gardenia', 'Classic Loaf', 80.00, '09/15/2023', '09/09/2023')

    # Make the supplier
    supplier = Supplier("TC Trading", 'Pandi')

    # Add supply to the supplier
    supply_1 = supplier.add_supply(coke_zero, 10)
    supply_2 = supplier.add_supply(gardenia, 10)

    # Make store
    store = Store('Adam Store', 'Pandi')

    # Display list of supply [Supplier]
    supplier.display_list_of_supplies()

    # Deliver supply to store
    supplier.deliver_supply(supply_1, 5, store)
    supplier.deliver_supply(supply_2, 5, store)

    # Display list of supply [Supplier]
    supplier.display_list_of_supplies()

    # Display available products
    store.display_products()

    # Display expired products
    store.display_expired_products()

    # Return the products to the supplier
    store.return_product(supplier)
