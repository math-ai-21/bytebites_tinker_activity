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
