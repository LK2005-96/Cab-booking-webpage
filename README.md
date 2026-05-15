# 🚕 SwiftCab — Cab Booking App

A lightweight cab booking application built with Python (Tkinter) and SQLite, featuring a step-by-step booking flow: login → destination → passenger details → driver selection.

---

## 📁 Recommended File Structure

Keep only these files in your repository:

```
Cab-booking-webpage/
├── index.html          ← Web version (single-file, no dependencies)
├── main.py             ← Main Python/Tkinter app (rename from "project taxi 22.py")
├── database.py         ← All DB operations (login, insert, fetch)
├── Users.db            ← SQLite database
├── assets/
│   ├── image1.png      ← Login screen background
│   ├── image2.png      ← Destination screen background
│   └── image3.png      ← Details screen background
└── README.md
```

> **Cleanup tip:** Delete `delete.py`, `deletr.py`, `count.py`, `updating.py`, `p testing.py`, `project testing 1.py`, `task 1.py`, `tea shop.py`, `testing.py`, `g cab.py`, `project taxi.py`, `DB_UPDATE.py`, and all duplicate/loose images. These are scratch files and do not belong in the final repo.

---

## ✨ Features

- **Login screen** — Username & password authentication against local DB
- **Destination form** — Pickup and drop point input with validation
- **Passenger details** — Number of passengers and contact number
- **Driver selection** — List of available drivers with vehicle numbers
- **Booking confirmation** — Success message on booking

---

## 🚀 How to Run

### Web Version (No install needed)
Just open `index.html` in any browser — no server or Python required.

### Python Version

**Requirements**
- Python 3.x
- Tkinter (built into Python)
- SQLite3 (built into Python)

**Steps**
```bash
git clone https://github.com/LK2005-96/Cab-booking-webpage.git
cd Cab-booking-webpage
python main.py
```

You'll see the login screen. Use any of the credentials below.

---

## 🔑 Default Login Credentials

| Username   | Password    |
|------------|-------------|
| Dom        | Dom3        |
| Brain      | Brain5      |
| Driver     | Driver6     |
| Travis     | Travis6     |
| Ken Miles  | Ken Miles8  |
| Frank      | Frank5      |

---

## 🗺️ Booking Flow

```
Login → Destination → Passenger Details → Pick a Driver → Confirmed ✓
```

---

## 🛠️ Tech Stack

| Layer     | Technology          |
|-----------|---------------------|
| GUI       | Python Tkinter      |
| Database  | SQLite3 (`Users.db`)|
| Web UI    | HTML / CSS / JS     |

---

## 📌 Known Limitations & Future Improvements

- [ ] Passwords are stored in plain text — add hashing (e.g. `bcrypt`)
- [ ] No real-time driver tracking
- [ ] MySQL support is commented out — can be re-enabled
- [ ] No user registration flow
- [ ] Mobile app not connected to a backend API

---

## 📄 License

MIT License — free to use and modify.
