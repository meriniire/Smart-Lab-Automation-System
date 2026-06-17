# Smart-Lab-Automation-System
A Streamlit-based laboratory management system for real-time workstation monitoring, issue reporting, reservations, maintenance tracking, and analytics.

# 🔬 Smart Lab Automation System

A modern laboratory management and monitoring platform built with Streamlit. The system enables real-time workstation monitoring, issue tracking, reservation management, maintenance oversight, and usage analytics for computer laboratories.

---

## 📖 Overview

The Smart Lab Automation System helps educational institutions efficiently manage computer laboratories through a centralized dashboard.

The platform provides:

* Real-time workstation monitoring
* Issue reporting and tracking
* Laboratory reservation management
* Maintenance monitoring
* Usage analytics and reporting
* Role-based access simulation

---

## ✨ Features

### 🏠 Dashboard

* Live workstation status overview
* Laboratory occupancy monitoring
* Active issue alerts
* System metrics and summaries

### 🖥️ Workstation Monitoring

* Track workstation availability
* View workstation IP addresses
* Status distribution charts
* Real-time visualization

### 📝 Issue Reporting

* Report hardware/software problems
* Assign severity levels
* Generate issue IDs automatically
* Track issue lifecycle

### 📋 Issue Management

* View all reported issues
* Resolve issues
* Technician and administrator controls

### 📅 Reservation System

* Laboratory booking requests
* Faculty and administrator access
* Schedule management

### 📊 Reporting & Analytics

* Usage reports
* Issue history reports
* Maintenance tracking
* CSV export functionality

### 🎨 Modern UI

* Responsive design
* Professional dashboard styling
* Interactive charts using Plotly
* Mobile-friendly interface

---

## 🛠️ Technology Stack

| Technology  | Purpose                   |
| ----------- | ------------------------- |
| Python      | Backend Logic             |
| Streamlit   | Web Application Framework |
| Pandas      | Data Processing           |
| NumPy       | Data Simulation           |
| Plotly      | Data Visualization        |
| CSV Storage | Lightweight Database      |

---

## 📂 Project Structure

```text
smart-lab-automation-system/
│
├── app.py
├── requirements.txt
├── README.md
├── LICENSE
├── .gitignore
│
├── lab_data/
│   ├── laboratories.csv
│   ├── workstations.csv
│   ├── issues.csv
│   └── reservations.csv
│
└── screenshots/
    └── dashboard.png
```

---

## 🚀 Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/smart-lab-automation-system.git

cd smart-lab-automation-system
```

### Create Virtual Environment

#### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

#### Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run Application

```bash
streamlit run app.py
```

The application will open in your browser:

```text
http://localhost:8501
```

---

## 👥 User Roles

### Student

* Report issues
* View workstation status

### Faculty

* Report issues
* Request reservations

### Technician

* Monitor systems
* Resolve issues

### Administrator

* Full system access
* Reservation approval
* Issue management

---

## 📊 Data Storage

The application currently uses CSV files as a lightweight data storage solution.

Files generated automatically:

* laboratories.csv
* workstations.csv
* issues.csv
* reservations.csv

For production deployment, consider replacing CSV storage with:

* PostgreSQL
* MySQL
* SQLite
* MongoDB

---

## 🔮 Future Enhancements

* IoT workstation integration
* RFID-based attendance
* Email notifications
* SMS alerts
* User authentication
* Database integration
* Predictive maintenance analytics
* Cloud deployment

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch
3. Commit changes
4. Submit a pull request

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

Developed as a Smart Laboratory Management Solution for educational institutions.

---

### ⭐ If you find this project useful, consider giving it a star.

