from flask import Flask, render_template, request

app = Flask(__name__)

# ===== OOP CLASSES =====
class Food:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_info(self):
        return f"{self.name} - ₹{self.price}"

class Dish(Food):
    category = "Main Course"

class Drink(Food):
    category = "Drink"

class Dessert(Food):
    category = "Dessert"

# ===== MENU DATA =====
menu_items = [
    Dish("Sivagangai Chicken Biryani", 150),
    Dish("Sivagangai Mutton Biryani", 200),
    Dish("Dosa", 50),
    Dish("Parotta", 40),
    Dish("Idly", 30),
    Drink("Coke", 20),
    Drink("Pepsi", 30),
    Drink("Torino", 25),
    Drink("Bovonto", 25),
    Dessert("Vanilla Ice Cream", 40),
    Dessert("Chocolate Ice Cream", 50),
    Dessert("Strawberry Ice Cream", 60),
    Dessert("Fruit Salad", 80),
]

# ===== STORE ORDERS =====
orders = []

# ===== ROUTES =====
@app.route("/")
def index():
    return render_template("home.html")

@app.route("/menu")
def menu():
    # Group items by category for menu page styling
    dishes = [item for item in menu_items if isinstance(item, Dish)]
    drinks = [item for item in menu_items if isinstance(item, Drink)]
    desserts = [item for item in menu_items if isinstance(item, Dessert)]
    return render_template("menu.html", dishes=dishes, drinks=drinks, desserts=desserts)

@app.route("/order", methods=["POST"])
def order():
    try:
        new_orders = []
        for item in menu_items:
            qty_str = request.form.get(item.name)
            if qty_str and qty_str.isdigit():
                qty = int(qty_str)
                if qty > 0:
                    new_orders.append({
                        "item": item.name,
                        "price": item.price,
                        "quantity": qty
                    })

        if not new_orders:
            raise ValueError("No items selected")

        orders.clear()  # reset previous order for new one
        orders.extend(new_orders)

        total_amount = sum(o["price"] * o["quantity"] for o in orders)

        return render_template("order.html", orders=orders, total=total_amount)

    except Exception as e:
        print(f"Order processing error: {e}")
        return "Error processing your order. Please try again.", 500

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
