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
- Automatically show mock flights even if exact results are not found

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
│ │ │ └── index.html # Main UI template (Jinja2)
│ │ └── static/
│ │ └── styles.css # Custom styles
│ └── frontend/ # (Optional placeholder for future assets)

yaml
Copy
Edit

---

## 🚀 How to Run the Project Locally

### ✅ Prerequisites:
- Python 3.8+ installed
- Flask installed (`pip install flask`)

### 🛠 Steps:

1. **Clone this repository:**
```bash
git clone https://github.com/<your-username>/flydreamair-booking.git
cd flydreamair-booking/src/backend
Install dependencies:

bash
Copy
Edit
pip install flask
Run the Flask app:

bash
Copy
Edit
python app.py
Open your browser and go to:

cpp
Copy
Edit
http://127.0.0.1:5000
👥 Team Members
Name	Student ID	Role	Contribution
Deon Pathrose Sunny	8150667	Project Manager	Contributed
Ashlin Lal	[Insert ID]	Analyst / Developer	Contributed
[Member 3 Name]	[Insert ID]	Designer	Almost No Contribution
[Member 4 Name]	[Insert ID]	Tester	Contributed

Contribution evaluations are included in the final project report.

✅ Features Implemented
 User login with session-based access

 Search flights by city and date

 List available mock flights

 Seat selection via dropdown

 Meal preference selection

 Unique booking ID generation

 Edit seat or meal via booking ID

 JSON-based data storage (no external DB required)

🧪 Testing
Test search with any origin/destination/date – mock flights are always shown.

Test booking and check bookings.json for your record.

Try editing a booking using the booking ID shown after confirmation.

📋 License
This project is intended solely for academic demonstration purposes as part of CSIT214 (University of Wollongong). Not licensed for production or commercial deployment.

Made with ❤️ by Team FlyDreamAir – 2025
