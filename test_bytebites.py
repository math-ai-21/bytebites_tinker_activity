from models import FoodItem, Menu, Transaction
#Category filtering
def test_filter_by_category_returns_matching_items():
   menu = Menu()
   soda = FoodItem("Large Soda", 1.75, "Drinks", 3.9)
   lemonade = FoodItem("Lemonade", 2.25, "Drinks", 4.5)
   burger = FoodItem("Spicy Burger", 6.50, "Mains", 4.7)
   for item in [soda, lemonade, burger]:
       menu.add_item(item)
   drinks = menu.filter_by_category("Drinks")
   assert set(drinks) == {soda, lemonade}

def test_filter_by_category_no_matches_returns_empty_list():
   menu = Menu()
   menu.add_item(FoodItem("Spicy Burger", 6.50, "Mains", 4.7))
   assert menu.filter_by_category("Desserts") == []

def test_filter_by_category_on_empty_menu():
   empty_menu = Menu()
   assert empty_menu.filter_by_category("Drinks") == []

def test_filter_by_category_is_case_sensitive():
   # Documents current behavior: "drinks" != "Drinks".
   menu = Menu()
   menu.add_item(FoodItem("Large Soda", 1.75, "Drinks", 3.9))
   assert menu.filter_by_category("drinks") == []

#Sorting
# Menu doesn't have its own sort method (not in the spec), so these tests
# sort the plain list of FoodItems directly with Python's built-in sorted().

def test_sort_items_by_price_ascending():
   menu = Menu()
   burger = FoodItem("Spicy Burger", 6.50, "Mains", 4.7)
   fries = FoodItem("Fries", 2.50, "Sides", 4.2)
   soda = FoodItem("Large Soda", 1.75, "Drinks", 3.9)
   for item in [burger, fries, soda]:
       menu.add_item(item)
   result = sorted(menu.items, key=lambda item: item.price)
   assert [item.name for item in result] == ["Large Soda", "Fries", "Spicy Burger"]

def test_sort_items_by_popularity_descending():
   menu = Menu()
   burger = FoodItem("Spicy Burger", 6.50, "Mains", 4.7)
   fries = FoodItem("Fries", 2.50, "Sides", 4.2)
   soda = FoodItem("Large Soda", 1.75, "Drinks", 3.9)
   for item in [burger, fries, soda]:
       menu.add_item(item)
   result = sorted(menu.items, key=lambda item: item.popularity_rating, reverse=True)
   assert [item.name for item in result] == ["Spicy Burger", "Fries", "Large Soda"]

def test_sort_single_item_menu():
   menu = Menu()
   soda = FoodItem("Large Soda", 1.75, "Drinks", 3.9)
   menu.add_item(soda)
   result = sorted(menu.items, key=lambda item: item.price)
   assert result == [soda]

def test_sort_empty_menu():
   menu = Menu()
   result = sorted(menu.items, key=lambda item: item.price)
   assert result == []

#Total calculation
def test_calculate_total_with_multiple_items():
   burger = FoodItem("Spicy Burger", 6.50, "Mains", 4.7)
   fries = FoodItem("Fries", 2.50, "Sides", 4.2)
   order = Transaction([burger, fries])
   assert order.calculate_total_cost() == 9.00

def test_calculate_total_with_single_item():
   soda = FoodItem("Large Soda", 1.75, "Drinks", 3.9)
   order = Transaction([soda])
   assert order.calculate_total_cost() == 1.75

def test_order_total_is_zero_when_empty():
   order = Transaction([])
   assert order.calculate_total_cost() == 0

def test_calculate_total_called_twice_is_consistent():
   burger = FoodItem("Spicy Burger", 6.50, "Mains", 4.7)
   order = Transaction([burger])
   first = order.calculate_total_cost()
   second = order.calculate_total_cost()
   assert first == second