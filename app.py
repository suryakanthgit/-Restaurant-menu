from flask import Flask, render_template, request
import mysql.connector
import os

app = Flask(__name__)


def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "db"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", "password"),
        database=os.getenv("DB_NAME", "restaurantdb"),
        port=int(os.getenv("DB_PORT", 3306))
    )


@app.route("/")
def index():
    return render_template("home.html")


@app.route("/menu")
def menu():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM menu_items")
    items = cursor.fetchall()

    cursor.close()
    conn.close()

    dishes = [item for item in items if item["category"] == "Main Course"]
    drinks = [item for item in items if item["category"] == "Drink"]
    desserts = [item for item in items if item["category"] == "Dessert"]

    return render_template("menu.html", dishes=dishes, drinks=drinks, desserts=desserts)


@app.route("/order", methods=["POST"])
def order():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT * FROM menu_items")
        menu_items = cursor.fetchall()

        new_orders = []
        total_amount = 0

        for item in menu_items:
            qty_str = request.form.get(item["name"])
            if qty_str and qty_str.isdigit():
                qty = int(qty_str)
                if qty > 0:
                    item_total = item["price"] * qty
                    total_amount += item_total
                    new_orders.append({
                        "menu_item_id": item["id"],
                        "item": item["name"],
                        "price": item["price"],
                        "quantity": qty
                    })

        if not new_orders:
            cursor.close()
            conn.close()
            return "No items selected", 400

        cursor.execute(
            "INSERT INTO orders (total_amount) VALUES (%s)",
            (total_amount,)
        )
        order_id = cursor.lastrowid

        for order_item in new_orders:
            cursor.execute(
                """
                INSERT INTO order_items (order_id, menu_item_id, quantity, price_each)
                VALUES (%s, %s, %s, %s)
                """,
                (
                    order_id,
                    order_item["menu_item_id"],
                    order_item["quantity"],
                    order_item["price"]
                )
            )

        conn.commit()

        cursor.close()
        conn.close()

        return render_template("order.html", orders=new_orders, total=total_amount)

    except Exception as e:
        print(f"Order processing error: {e}")
        return "Error processing your order. Please try again.", 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
