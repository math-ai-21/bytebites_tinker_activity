#The four classes are:
#Customer-gets the person's name and purchase history.
#FoodItem-contains the name of the food item, its price, category, and popularity rating.
#Menu-contains multiple food items and a method to filter by category.
#Transaction-contains a list of selected food items and the total cost of the items.
#The four classes are meant to simulate the actual processing of a customer ordering food and receiving the total cost of their selected items.
class Customer:
   # Represents a person using the app.
   # Depends on: Transaction (below in this file) for purchase_history entries.
   def __init__(self, name):
       self.name = name
       self.purchase_history = []  # list of Transaction

   def add_transaction(self, transaction):
       self.purchase_history.append(transaction)

class FoodItem:
   # A single item that can be sold, e.g. "Spicy Burger".
   def __init__(self, name, price, category, popularity_rating):
       self.name = name
       self.price = price
       self.category = category
       self.popularity_rating = popularity_rating

class Menu:
   # Holds every FoodItem the app can sell and lets us filter them.
   # Depends on: FoodItem (above in this file).
   def __init__(self):
       self.items = []  # list of FoodItem

   def add_item(self, food_item):
       self.items.append(food_item)

   def filter_by_category(self, category):
       # Returns only the FoodItems matching the given category (e.g. "Drinks").
       return [item for item in self.items if item.category == category]

class Transaction:
   # Represents one order: the items a customer picked and what they cost.
   # Depends on: FoodItem (above in this file).
   def __init__(self, selected_items):
       self.selected_items = selected_items  # list of FoodItem
       self.total_cost = 0

   def calculate_total_cost(self):
       # Adds up the price of every selected FoodItem and stores/returns it.
       self.total_cost = sum(item.price for item in self.selected_items)
       return self.total_cost
def main():
   # Small scenario: create and inspect a few sample objects, then
   # exercise add_item, sorting, filter_by_category, and calculate_total_cost.
   #Create sample FoodItems
   burger = FoodItem("Spicy Burger", 6.50, "Mains", 4.7)
   fries = FoodItem("Fries", 2.50, "Sides", 4.2)
   soda = FoodItem("Large Soda", 1.75, "Drinks", 3.9)
   lemonade = FoodItem("Lemonade", 2.25, "Drinks", 4.5)
   ice_cream = FoodItem("Ice Cream", 3.00, "Desserts", 4.8)

   print("Sample FoodItems:")
   for item in [burger, fries, soda, lemonade, ice_cream]:
       print(f"{item.name}: ${item.price} ({item.category}), popularity {item.popularity_rating}")

   #Add items to a Menu
   menu = Menu()
   for item in [burger, fries, soda, lemonade, ice_cream]:
       menu.add_item(item)

   print("\nMenu after adding items:")
   for item in menu.items:
       print(item.name)

   # Sort the menu's items
   # Menu doesn't have its own sort method (not in the spec), so we sort the
   # plain list of FoodItems directly using Python's built-in sorted().
   sorted_by_price = sorted(menu.items, key=lambda item: item.price)
   print("\nMenu sorted by price (low to high):")
   for item in sorted_by_price:
       print(f"{item.name}: ${item.price}")

   sorted_by_popularity = sorted(menu.items, key=lambda item: item.popularity_rating, reverse=True)
   print("\nMenu sorted by popularity (high to low):")
   for item in sorted_by_popularity:
       print(f"{item.name}: popularity {item.popularity_rating}")

   #Filter by category
   drinks = menu.filter_by_category("Drinks")
   print("\nDrinks only:")
   for item in drinks:
       print(item.name)

   #Create a Customer and place an order
   customer = Customer("Alex")
   order = Transaction([burger, fries, lemonade])
   total = order.calculate_total_cost()
   customer.add_transaction(order)

   print(f"\nOrder total for {customer.name}")
   print(f"Items: {[item.name for item in order.selected_items]}")
   print(f"Total cost: ${total}")
   print(f"Transactions in purchase history: {len(customer.purchase_history)}")

if __name__ == "__main__":
    main()
