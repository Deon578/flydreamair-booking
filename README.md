# ✈️ FlyDreamAir – Customer Management and Booking System

A flight booking and management system built as part of the **CSIT214 – IT Project Management** course at the **University of Wollongong**.

---

## 📌 Project Overview

This web application allows users to:
- Log in with name and email
- Search for available flights by origin, destination, and date
- Book a flight with seat selection and meal preference
- Receive a unique booking ID upon confirmation
- Edit an existing booking using the booking ID
- Automatically see results or mock flights if no exact match is found

---

## 🗂️ Repository Structure

flydreamair-booking/
├── src/
│ ├── backend/
│ │ ├── app.py # Main Flask application
│ │ ├── bookings.json # Stores confirmed bookings
│ │ ├── flights.json # Sample/mock flight data
│ │ ├── users.json # User login data
│ │ ├── templates/
│ │ │ └── index.html # Main UI template
│ │ └── static/
│ │ └── styles.css # Styling for frontend
│ └── frontend/ # (Optional placeholder for future static assets or JS)

---

## 🚀 How to Run the Project Locally

### Prerequisites:
- Python 3.8+ installed
- Flask installed (`pip install flask`)

### Steps:

1. **Clone this repository:**
```bash
git clone https://github.com/<your-username>/flydreamair-booking.git
cd flydreamair-booking/src/backend

pip install flask

python app.py

http://127.0.0.1:5000
👥 Team Members
Name	Student ID	Role	Contribution
Deon Pathrose Sunny	8150667	Project Manager	Contributed
Ashlin Lal	[Insert ID]	Analyst / Developer	Contributed
[Member 3 Name]	[Insert ID]	Designer	Almost No Contribution
[Member 4 Name]	[Insert ID]	Tester	Contributed

Contribution details are included in the final project report.

🛠 Features Implemented
 Search and list available flights

 Book flights with seat & meal selection

 Generate unique booking IDs

 Update booking using booking ID

 Show available seats dynamically

 JSON-based backend (no DB required)

🧪 Testing
Run the app and use different combinations of origin, destination, and date.

Try editing a booking using the ID provided after booking confirmation.

All data is stored in JSON files (bookings.json, users.json).

📋 License
This project is submitted for academic purposes and not intended for commercial use.

Made with ❤️ by Team FlyDreamAir – University of Wollongong, 2025.
