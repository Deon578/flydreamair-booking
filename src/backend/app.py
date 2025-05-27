from flask import Flask, render_template, request, redirect, url_for, session
import json, os, random
from datetime import datetime

app = Flask(__name__)
app.secret_key = "flydreamair-secret"

FLIGHTS_FILE = "flights.json"
BOOKINGS_FILE = "bookings.json"
USERS_FILE = "users.json"

# -------------------- Utility Functions --------------------

def load_flights():
    if os.path.exists(FLIGHTS_FILE):
        with open(FLIGHTS_FILE, "r") as f:
            return json.load(f)
    return []

def save_booking(booking):
    if os.path.exists(BOOKINGS_FILE):
        with open(BOOKINGS_FILE, "r") as f:
            bookings = json.load(f)
    else:
        bookings = []
    bookings.append(booking)
    with open(BOOKINGS_FILE, "w") as f:
        json.dump(bookings, f, indent=2)

def get_available_seats(flight_number):
    all_seats = [f"{row}{col}" for row in "ABCDEF" for col in range(1, 11)]
    if os.path.exists(BOOKINGS_FILE):
        with open(BOOKINGS_FILE, "r") as f:
            bookings = json.load(f)
        booked = [b["seat"] for b in bookings if b["flight_number"] == flight_number]
        return [seat for seat in all_seats if seat not in booked]
    return all_seats

def generate_booking_id():
    return f"BK{datetime.now().strftime('%Y%m%d')}-{random.randint(100000, 999999)}"

# -------------------- Routes --------------------

@app.route("/", methods=["GET"])
def index():
    if "username" not in session:
        return render_template("index.html", flights=None)

    flights = load_flights()
    available_seats = get_available_seats(flights[0]["flight_number"]) if flights else []
    return render_template("index.html", flights=flights, available_seats=available_seats)

@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    email = request.form["email"]
    session["username"] = username

    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, "r") as f:
            users = json.load(f)
    else:
        users = []

    users.append({"username": username, "email": email})
    with open(USERS_FILE, "w") as f:
        json.dump(users, f, indent=2)

    return redirect(url_for("index"))

@app.route("/search", methods=["POST"])
def search():
    if "username" not in session:
        return redirect(url_for("index"))

    origin = request.form["origin"].strip().title()
    destination = request.form["destination"].strip().title()
    date = request.form["date"].strip()

    flights = load_flights()
    matched = [
        f for f in flights
        if origin in f["origin"] and destination in f["destination"]
    ]

    if not matched:
        mock_flight = {
            "flight_number": "FX" + str(random.randint(100, 999)),
            "origin": origin,
            "destination": destination,
            "date": date,
            "time": "10:00",
            "aircraft": "Boeing 737"
        }
        matched = [mock_flight]

    available_seats = get_available_seats(matched[0]["flight_number"])
    return render_template("index.html", flights=matched, available_seats=available_seats)

@app.route("/book", methods=["POST"])
def book():
    if "username" not in session:
        return redirect(url_for("index"))

    flight_number = request.form["flight_number"]
    seat = request.form["seat"]
    meal = request.form["meal"]
    username = session["username"]
    booking_id = generate_booking_id()

    booking = {
        "booking_id": booking_id,
        "username": username,
        "flight_number": flight_number,
        "seat": seat,
        "meal": meal
    }

    save_booking(booking)
    return f"<h2>Booking confirmed!</h2><p>Booking ID: <strong>{booking_id}</strong></p><p><a href='/'>Back to home</a></p>"

@app.route("/edit-booking", methods=["POST"])
def edit_booking():
    booking_id = request.form["booking_id"]
    new_seat = request.form["new_seat"]
    new_meal = request.form["new_meal"]

    if os.path.exists(BOOKINGS_FILE):
        with open(BOOKINGS_FILE, "r") as f:
            bookings = json.load(f)
    else:
        bookings = []

    updated = False
    for b in bookings:
        if b["booking_id"] == booking_id:
            if new_seat:
                b["seat"] = new_seat
            if new_meal:
                b["meal"] = new_meal
            updated = True

    with open(BOOKINGS_FILE, "w") as f:
        json.dump(bookings, f, indent=2)

    if updated:
        return f"<h2>Booking updated!</h2><p>Booking ID: <strong>{booking_id}</strong></p><p><a href='/'>Back to home</a></p>"
    else:
        return "<h2>Booking ID not found.</h2><p><a href='/'>Back to home</a></p>"

# -------------------- Main --------------------

if __name__ == "__main__":
    app.run(debug=True)
