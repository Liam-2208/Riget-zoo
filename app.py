#Helped by Liam-2208 / Liam Filer on the same MAC 
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/signup")
def signup():
    return render_template("signup.html")


@app.route("/hotel")
def hotel():
    return render_template("hotel.html")


@app.route("/tickets")
def tickets():
    return render_template("tickets.html")


@app.route("/purchase", methods=["POST"])
def purchase():
    ticket_type = request.form.get("ticket_type")

    prices = {
        "adult": 18,
        "child": 10,
        "family": 45
    }
    price = prices.get(ticket_type, 0)

    return render_template(
        "confirmation.html",
        ticket_type=ticket_type.capitalize(),
        price=price
    )


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template("500.html"), 500


if __name__ == "__main__":
    app.run(debug=True)
