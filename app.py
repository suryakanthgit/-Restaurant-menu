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
@app.route("/order", methods=["GET", "POST"])
def order():
    total_price = None

    if request.method == "POST":
        try:
            price = int(request.form.get("price", 0))
            quantity = int(request.form.get("quantity", 1))
            total_price = price * quantity
        except ValueError:
            total_price = "Invalid input"

    return render_template("order.html", total_price=total_price)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
