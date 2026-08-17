class item:
def _init_(self,name,price):
  self.name = name #item name
  self.price = price #item price 
class inventory:
  def _init_(self): 
    self.items = [] #List to store items added to inventory 
  def add_item(self,item,item.stock): 
    #add items to inventory with specified quantity 
    self.items.append((item,quantity)) 
  def remove_item(self, item_name):
    #removes item from inventory based on name
        self.items = [item for item in self.items if item[0].name != item_name]
  def display_inventory(self): 
    print("\n Current Inventory")
    #displays inventory 
    for item, quantity in self.items:
            print(f"{item.name}: {quantity}")
class InventorySystem: 
  def _init_(self): 
     self.inventory = inventory()
    def add_item_to_inventory(self):
        # Allows user to add an item to inventory
        name = input("Enter item name: ")
        price = float(input(f"Enter price of {name}: $"))
        quantity = int(input(f"Enter quantity of {name}: "))
        item = item(name, price)
        self.inventory.add_item(item, quantity)
        print(f"Added {quantity} x {name} to inventory.")
    def remove_item_from_inventory(self):
        # Allows user to remove an item from the cart
        item_name = input("Enter item name to remove: ")
        self.inventory.remove_item(item_name)
        print(f"Removed {item_name} from inventory.")
    def run(self):
        # Main function to run the inventory system
        while True:
            print("\nInventory System")
            print("1. Add Item to inventory")
            print("2. Remove Item from inventory")
            print("3. Process Payment")
            print("4. Exit")

            choice = input("Choose an option: ")
            if choice == '1':
                self.add_item_to_inventory()
            elif choice == '2':
                self.remove_item_from_inventory()
            elif choice == '3':
                self.process_payment()
                break
            elif choice == '4':
                print("Exiting Inventory System.")
                break
            else:
                print("Invalid option. Try again.")
    
      

  
