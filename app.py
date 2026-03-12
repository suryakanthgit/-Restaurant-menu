from flask import Flask, render_template, request

app = Flask(__name__)

# Home page
@app.route("/")
def home():
    return render_template("home.html")


# Menu page
@app.route("/menu")
def menu():
    dishes = [
        {"name": "Sivagangai Chicken Biryani", "price": 150},
        {"name": "Sivagangai Mutton Biryani", "price": 200},
        {"name": "Plain Dosa", "price": 50},
        {"name": "Parotta", "price": 40},
        {"name": "Idly", "price": 30}
    ]

    drinks = [
        {"name": "Coke", "price": 20},
        {"name": "Pepsi", "price": 20},
        {"name": "Sprite", "price": 20},
        {"name": "Fresh Lime Juice", "price": 30}
    ]

    desserts = [
        {"name": "Vanilla Ice Cream", "price": 40},
        {"name": "Fruit Salad", "price": 80},
        {"name": "Gulab Jamun", "price": 35}
    ]

    return render_template(
        "menu.html",
        dishes=dishes,
        drinks=drinks,
        desserts=desserts
    )


# Order page
@app.route("/order", methods=["POST"])
def order():
    orders = []
    total = 0

    menu_prices = {
        "Sivagangai Chicken Biryani": 150,
        "Sivagangai Mutton Biryani": 200,
        "Plain Dosa": 50,
        "Parotta": 40,
        "Idly": 30,
        "Coke": 20,
        "Pepsi": 20,
        "Sprite": 20,
        "Fresh Lime Juice": 30,
        "Vanilla Ice Cream": 40,
        "Fruit Salad": 80,
        "Gulab Jamun": 35
    }

    for item, price in menu_prices.items():
        qty = int(request.form.get(item, 0))

        if qty > 0:
            subtotal = price * qty
            orders.append({
                "item": item,
                "price": price,
                "quantity": qty,
                "subtotal": subtotal
            })
            total += subtotal

    return render_template("order.html", orders=orders, total=total)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
