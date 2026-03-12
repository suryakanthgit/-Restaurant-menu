from flask import Flask, render_template, request

app = Flask(__name__)

# Home page
@app.route("/")
def home():
    return render_template("home.html")


# Menu page
@app.route("/menu", methods=["GET", "POST"])
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

    # When user clicks "Place Order"
    if request.method == "POST":

        orders = []
        total = 0

        all_items = dishes + drinks + desserts

        for item in all_items:

            qty = int(request.form.get(item["name"], 0))

            if qty > 0:

                subtotal = item["price"] * qty

                orders.append({
                    "item": item["name"],
                    "price": item["price"],
                    "quantity": qty,
                    "subtotal": subtotal
                })

                total += subtotal

        return render_template("order.html", orders=orders, total=total)

    return render_template(
        "menu.html",
        dishes=dishes,
        drinks=drinks,
        desserts=desserts
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
