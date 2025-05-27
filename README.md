
# ✈️ FlyDreamAir – Customer Management and Booking System

A comprehensive and user-centric web application for **flight booking, seat management, and customer interaction**, developed as part of the **CSIT214 – IT Project Management** course at the **University of Wollongong**.

[Our website can be accessed here](https://deonpsunny1.wixsite.com/flydreamair-booking).
---

## 🌟 Project Highlights

FlyDreamAir Booking System aims to **modernize airline booking services** by delivering a full-featured platform where users can:

- Log in with name and email  
- Search flights dynamically (any city, any date – always returns a match!)  
- Select seats and meal preferences  
- Automatically receive a **unique Booking ID**
- View available flights instantly
- Edit bookings using Booking ID
- Enjoy an intuitive, responsive, and colorful UI  
- Experience a functional simulation that closely mimics a real-world airline booking system

🎯 **All functionalities are backed by structured JSON data**, making it easy to update, scale, and enhance in the future.

---

## 👥 Team Members

| Name                | Student ID | Role               | Contribution                          |
|---------------------|------------|--------------------|---------------------------------------|
| Deon Pathrose Sunny | 8150667    |   Programmer       | Website, front/back end, coordination |
| Ashlin Lal          |  |  Prersentation    | Built UI, search & booking features |
| Yizhe LU            |  |   Documentation   | [Contribution]           |
| Zeyu Xie            |  | Interface Design  | [Contribution]           |

---

## 🧰 Technologies Used

- **Python** (Flask)
- **HTML/CSS** (custom layout + inline styles)
- **Jinja2 Templating**
- **JSON** for dynamic flight/user/booking data
- Hosted locally; no external databases needed

---

## 📂 Repository Structure

```
flydreamair-booking-system/
├── backend/                  # Python Flask app & data
│   ├── app.py
│   ├── flights.json
│   ├── bookings.json
│   ├── users.json
│   └── README.md
├── frontend/                 # Frontend layout and static content
│   ├── templates/
│   │   └── index.html
│   ├── static/
│   │   └── styles.css
│   └── README.md
├── README.md                 # Main project overview (this file)
```

---

## 🚀 How to Run the Project

1. **Install Python** (v3.10 or higher)
2. Clone the repository:
   ```bash
   git clone https://github.com/your-group-id/flydreamair-booking-system.git
   cd flydreamair-booking-system/backend
   ```
3. Run the app:
   ```bash
   python app.py
   ```
4. Open your browser and go to:  
   `http://127.0.0.1:5000`

✅ No need for external database. Everything runs with local JSON storage.

---

## 📈 Why This Project Stands Out

This system was carefully designed with **realistic project management** practices and a **clear user-focused interface**, reflecting:

- Solid project planning (scope, WBS, risk management, etc.)
- Agile-inspired development (tested weekly, incrementally improved)
- Version control via GitHub
- Dynamic, real-time user input handling
- Clean, simple code architecture

---

## 🏁 Final Notes

This submission fulfills all required features for the CSIT214 project. It showcases how **thoughtful design + agile coding + teamwork** results in a powerful system that's easy to use and maintain.

---

> Built with passion, precision, and Python 🐍  
> Team FlyDreamAir ✈️ – 2025
