
# ✈️ FlyDreamAir – Customer Management and Booking System

A full-stack airline booking system built as part of **CSIT214 – IT Project Management** at the **University of Wollongong**.

---

## 📝 Project Overview

FlyDreamAir Booking System enables users to:
- Log in with credentials
- Search flights by destination and date
- Book flights with seat and meal preferences
- Edit bookings via a unique booking ID
- View always-available mock flights for any input

---

## 🗂️ Repository Structure

```
flydreamair-booking/
├── README.md                 # Main project overview
├── src/
│   ├── frontend/             # UI assets (HTML/CSS)
│   │   └── README.md
│   └── backend/              # Flask backend and data
│       └── README.md
```

---

## 👨‍💻 Team Members

| Name                | Student ID | Role                | Contribution             |
|---------------------|------------|---------------------|--------------------------|
| Deon Pathrose Sunny | 8150667    | Project Manager     | Contributed              |
| Ashlin Lal          | [Insert ID] | Analyst / Developer | Contributed              |
| [Member 3 Name]     | [Insert ID] | Designer            | Almost No Contribution   |
| [Member 4 Name]     | [Insert ID] | Tester              | Contributed              |

---

## ⚙️ Running the Project

### Prerequisites:
- Python 3.8 or higher
- Flask (`pip install flask`)

### Setup:
```bash
cd src/backend
python app.py
```
Then visit: `http://127.0.0.1:5000`

---

## ✅ Key Features

- 🔐 User login
- ✈️ Search and view all flights (mock data)
- 🧾 Book flights (with seat/meal selection)
- 🔄 Edit bookings via booking ID
- 📄 JSON-based storage (no DB required)

---

## 📂 JSON Data Files

- `flights.json`: Pre-defined flight listings
- `bookings.json`: Stores all confirmed bookings
- `users.json`: Stores login session info

---

## 🧪 Testing Suggestions

- Try booking a flight with various city names and dates – flights will always appear
- Booking ID is auto-generated and displayed after confirmation
- You can update your seat or meal using the Edit Booking form

---

## 📄 License

Academic Use Only – Project for CSIT214, University of Wollongong
