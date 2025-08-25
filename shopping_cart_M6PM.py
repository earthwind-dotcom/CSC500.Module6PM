class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0.0, item_quantity=0, item_description="none"):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description
    
    def print_item_cost(self):
        total = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${total}")
    
    def print_item_description(self):
        print(f"{self.item_name}: {self.item_description}")


class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []
    
    def add_item(self, item):
        self.cart_items.append(item)
    
    def remove_item(self, item_name):
        found = False
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                found = True
                break
        
        if not found:
            print("Item not found in cart. Nothing removed.")
    
    def modify_item(self, modified_item):
        found = False
        for i, item in enumerate(self.cart_items):
            if item.item_name == modified_item.item_name:
                found = True
                # Only update if the new values are not default
                if modified_item.item_quantity != 0:
                    self.cart_items[i].item_quantity = modified_item.item_quantity
                if modified_item.item_price != 0.0:
                    self.cart_items[i].item_price = modified_item.item_price
                if modified_item.item_description != "none":
                    self.cart_items[i].item_description = modified_item.item_description
                break
        
        if not found:
            print("Item not found in cart. Nothing modified.")
    
    def get_num_items_in_cart(self):
        total_quantity = 0
        for item in self.cart_items:
            total_quantity += item.item_quantity
        return total_quantity
    
    def get_cost_of_cart(self):
        total_cost = 0
        for item in self.cart_items:
            total_cost += (item.item_price * item.item_quantity)
        return total_cost
    
    def print_total(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        num_items = self.get_num_items_in_cart()
        print(f"Number of Items: {num_items}")
        print()
        
        if num_items == 0:
            print("SHOPPING CART IS EMPTY")
        else:
            for item in self.cart_items:
                item.print_item_cost()
        
        print()
        total_cost = self.get_cost_of_cart()
        print(f"Total: ${total_cost}")
        print()
    
    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print()
        print("Item Descriptions")
        for item in self.cart_items:
            item.print_item_description()
        print()


def print_menu(cart):
    menu = """
MENU
a - Add item to cart
r - Remove item from cart
c - Change item quantity
i - Output items' descriptions
o - Output shopping cart
q - Quit
"""
    print(menu)
    
    while True:
        choice = input("Choose an option: ").strip().lower()
        
        if choice == 'a':
            add_item_to_cart(cart)
            return True
        elif choice == 'r':
            remove_item_from_cart(cart)
            return True
        elif choice == 'c':
            change_item_quantity(cart)
            return True
        elif choice == 'i':
            cart.print_descriptions()
            return True
        elif choice == 'o':
            cart.print_total()
            return True
        elif choice == 'q':
            return False
        else:
            print("Invalid option. Please try again.")


def add_item_to_cart(cart):
    print("ADD ITEM TO CART")
    name = input("Enter the item name: ")
    description = input("Enter the item description: ")
    price = float(input("Enter the item price: "))
    quantity = int(input("Enter the item quantity: "))
    
    new_item = ItemToPurchase(name, price, quantity, description)
    cart.add_item(new_item)
    print()


def remove_item_from_cart(cart):
    print("REMOVE ITEM FROM CART")
    name = input("Enter name of item to remove: ")
    cart.remove_item(name)
    print()


def change_item_quantity(cart):
    print("CHANGE ITEM QUANTITY")
    name = input("Enter the item name: ")
    
    # Create a temporary item with just the name and new quantity
    new_quantity = int(input("Enter the new quantity: "))
    modified_item = ItemToPurchase(item_name=name, item_quantity=new_quantity)
    
    cart.modify_item(modified_item)
    print()


def main():
    # Get customer information
    customer_name = input("Enter customer's name: ")
    current_date = input("Enter today's date: ")
    print()
    
    # Create shopping cart
    cart = ShoppingCart(customer_name, current_date)
    
    # Display customer information
    print(f"Customer name: {customer_name}")
    print(f"Today's date: {current_date}")
    print()
    
    # Display menu and process choices until user quits
    continue_menu = True
    while continue_menu:
        continue_menu = print_menu(cart)


if __name__ == "__main__":
    main()