# ChronoAge Metrics 🗓️
### Precision Time-based Age Analysis

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=flat&logo=python)
![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-FF4B4B?style=flat&logo=streamlit)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat)

---

## 📌 Overview

**ChronoAge Metrics** is a clean and interactive web application built with **Streamlit** that calculates your precise age based on your date of birth. It goes beyond just showing years — it breaks down your entire life into months, weeks, and days, while also telling you how many days are left until your next birthday.

---

## ✨ Features

- 🎂 **Accurate Age Calculation** — Accounts for whether your birthday has passed this year or not
- 📅 **Next Birthday Countdown** — Days remaining until your next birthday
- 📊 **Detailed Time Breakdown** — Total months, weeks, and days lived
- ⏳ **Smooth UX** — Loading spinner for a polished user experience
- 📱 **Responsive Layout** — Two-column metric display using Streamlit columns

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core logic & calculations |
| Streamlit | Web UI framework |
| datetime | Date handling |

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- pip

### Installation

**1. Clone the repository**
```bash
git clone https://github.com/awasthi-anshika801/ChronoAge-Metrics.git
cd ChronoAge-Metrics
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Run the app**
```bash
streamlit run app.py
```

**4. Open in browser**
```
http://localhost:8501
```

---

## 📁 Project Structure

```
chronoage-metrics/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

---

## 📸 App Preview

> 🗓️ Select your date of birth → Click **Calculate Age** → Get your full time breakdown instantly!

**Metrics Displayed:**
- ✅ Current Age (in years)
- ✅ Days left for next birthday
- ✅ Total months lived
- ✅ Total weeks lived
- ✅ Total days lived

---

## 🧮 How It Works

1. User selects their **Date of Birth** from the date picker
2. App calculates the difference between **today's date** and the entered DOB
3. Adjusts age if the **birthday hasn't occurred yet** this year
4. Uses `30.4375` as average days per month *(365 ÷ 12)* for accurate month calculation
5. Calculates the **next birthday date** and finds the difference from today

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License**.

---

## 👨‍💻 Author

**Anshika Awasthi**
- 🌐 GitHub: [@awasthi-anshika801](https://github.com/awasthi-anshika801)
- 💼 LinkedIn: [anshika-awasthi-499083338](https://www.linkedin.com/in/anshika-awasthi-499083338/)
