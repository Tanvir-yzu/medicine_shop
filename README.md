
<div align="center">

# 💊 Medicine Shop Management System

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Python](https://img.shields.io/badge/python-3.8+-green)
![Django](https://img.shields.io/badge/django-4.0+-brightgreen)
![License](https://img.shields.io/badge/license-MIT-orange)

A modern, web-based pharmacy inventory management system built with Django and Tailwind CSS. Features a sleek UI, QR code scanning, and comprehensive medicine tracking capabilities.

[![Demo Video](https://img.shields.io/badge/demo-available-purple)](http://127.0.0.1:8000/)
[![Documentation](https://img.shields.io/badge/docs-wiki-informational)](#)

</div>

---

## ✨ Features

<div align="center">

### 🔐 Authentication
- Secure Google OAuth login
- User session management
- Protected routes

### 💊 Medicine Management
- Create, Read, Update, Delete (CRUD) operations
- Inventory tracking with stock alerts
- Expiry date monitoring
- Search and filter functionality

### 📱 QR Code System
- Generate QR codes for each medicine
- Scan QR codes for instant lookup
- Batch number tracking
- Fuzzy search fallback

### 🎨 Modern UI/UX
- Responsive design (mobile & desktop)
- Gradient backgrounds
- Smooth animations
- Dark mode ready
- Real-time notifications

### 📊 Dashboard
- Inventory statistics
- Low stock alerts
- Expiry warnings
- Visual data representation

</div>

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|-----------|
| **Backend** | ![Python](https://img.shields.io/badge/Python-3.8+-yellow) ![Django](https://img.shields.io/badge/Django-4.0+-green) |
| **Frontend** | ![HTML5](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white) ![Tailwind CSS](https://img.shields.io/badge/Tailwind-06B6D4?logo=tailwindcss&logoColor=white) |
| **Icons** | ![Font Awesome](https://img.shields.io/badge/Font%20Awesome-339AF0?logo=fontawesome&logoColor=white) |
| **Database** | ![SQLite](https://img.shields.io/badge/SQLite-003B57?logo=sqlite&logoColor=white) (Configurable to PostgreSQL/MySQL) |
| **QR Code** | ![html5-qrcode](https://img.shields.io/badge/html5--qrcode-2.3.8-blue) |
| **Search** | ![FuzzyWuzzy](https://img.shields.io/badge/FuzzyWuzzy-0.18.0-purple) |

---

## 📦 Installation

### Prerequisites

- ![Python](https://img.shields.io/badge/Python-3.8+-yellow) Python 3.8 or higher
- ![pip](https://img.shields.io/badge/pip-latest-blue) pip package installer
- ![VirtualEnv](https://img.shields.io/badge/Virtual-Environment-green) (recommended)

### Quick Start

#### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Tanvir-yzu/medicine_shop.git
cd medicine_shop
```

#### 2️⃣ Create Virtual Environment

<details>
<summary><b>Windows</b></summary>

```bash
python -m venv myenv
myenv\Scripts\activate
```

</details>

<details>
<summary><b>macOS / Linux</b></summary>

```bash
python3 -m venv myenv
source myenv/bin/activate
```

</details>

#### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

#### 4️⃣ Configure Project

Create a `.env` file in the project root:

```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

#### 5️⃣ Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

#### 6️⃣ Create Superuser

```bash
python manage.py createsuperuser
```

#### 7️⃣ Start Development Server

```bash
python manage.py runserver
```

#### 8️⃣ Access Application

- 🌐 **Main App**: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- 🔧 **Admin Panel**: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## 📖 Usage Guide

### Login Process

1. Visit the application URL
2. Click "Login with Google"
3. Authorize with your Google account
4. You'll be redirected to the dashboard

### Managing Medicines

| Action | Description |
|--------|-------------|
| **View Inventory** | Browse all medicines in a beautiful table layout |
| **Add Medicine** | Click "Add New Medicine" and fill out the form |
| **Scan QR Code** | Use camera to scan medicine QR codes |
| **Edit Details** | Click the edit icon to update medicine information |
| **Delete** | Remove medicines with confirmation dialog |

### Search & Filter

- Use the search bar to find medicines by name or batch number
- Fuzzy search helps find partial matches
- Real-time filtering as you type

---

## 📁 Project Structure

```
medicine_shop/
├── 📂 medicine_shop/          # Project configuration
│   ├── 📄 __init__.py
│   ├── ⚙️ settings.py         # Django settings
│   ├── 🌐 urls.py             # Main URL routes
│   └── 🚀 wsgi.py            # WSGI config
│
├── 📂 medicines/              # Main application
│   ├── 📂 templates/          # HTML templates
│   │   └── 📂 medicines/
│   │       ├── 🎨 base.html           # Base template
│   │       ├── 📋 medicine_list.html
│   │       ├── 📄 medicine_detail.html
│   │       ├── ➕ medicine_form.html
│   │       ├── 📷 scan_medicine.html
│   │       └── 🗑️ medicine_confirm_delete.html
│   ├── 📄 __init__.py
│   ├── 👤 admin.py            # Admin configuration
│   ├── 📱 apps.py
│   ├── 📂 migrations/         # Database migrations
│   ├── 🗃️ models.py           # Data models
│   ├── 🌐 urls.py             # App URL configuration
│   └── 🎮 views.py            # View logic
│
├── 📂 user/                   # User authentication app
│   ├── 📂 templates/
│   │   └── 📂 user/
│   │       └── 🔐 login.html
│   └── ...other files...
│
├── 📄 manage.py               # Django CLI
├── 📦 requirements.txt        # Dependencies
├── 📸 Photo/                  # Screenshots
└── 📖 README.md               # This file
```

---

## 🎨 Screenshots

### 🏠 Main Application

<div align="center">

<img src="./Photo/01.png" alt="Login Page" width="600">
<img src="./Photo/02.png" alt="Medicine List" width="600">
<img src="./Photo/03.png" alt="Add Medicine" width="600">
<img src="./Photo/04.png" alt="Medicine Details" width="600">
<img src="./Photo/05.png" alt="QR Scanner" width="600">

</div>

### 🔧 Admin Dashboard

<div align="center">

<img src="./Photo/06.png" alt="Admin Login" width="600">
<img src="./Photo/07.png" alt="Admin Dashboard" width="600">
<img src="./Photo/08.png" alt="Medicine Management" width="600">
<img src="./Photo/09.png" alt="Edit Medicine" width="600">

</div>

---

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. 🍴 **Fork** the repository
2. 🌿 **Create** a new branch (`git checkout -b feature/AmazingFeature`)
3. 💾 **Commit** your changes (`git commit -m 'Add some AmazingFeature'`)
4. 📤 **Push** to the branch (`git push origin feature/AmazingFeature`)
5. 🔀 **Open** a Pull Request

### Development Guidelines

- Follow PEP 8 style guidelines
- Write meaningful commit messages
- Add tests for new features
- Update documentation

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2025 Medicine Shop Management System

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction...
```

---

## 🙏 Acknowledgments

- [![Django](https://img.shields.io/badge/Django-092E20?logo=django&logoColor=white)](https://www.djangoproject.com/) The web framework for perfectionists with deadlines
- [![Tailwind CSS](https://img.shields.io/badge/Tailwind-06B6D4?logo=tailwindcss&logoColor=white)](https://tailwindcss.com/) Rapidly build modern websites without leaving your HTML
- [![Font Awesome](https://img.shields.io/badge/Font%20Awesome-339AF0?logo=fontawesome&logoColor=white)](https://fontawesome.com/) The internet's icon library
- [![html5-qrcode](https://img.shields.io/badge/html5--qrcode-blue)](https://github.com/mebjas/html5-qrcode) A cross-browser QR code scanning library

---

<div align="center">

## ⭐ Star This Project!

If you find this project helpful, please consider giving it a ⭐ star on GitHub!

[![GitHub stars](https://img.shields.io/github/stars/Tanvir-yzu/medicine_shop?style=social)](https://github.com/Tanvir-yzu/medicine_shop/stargazers)

---

Made with ❤️ by [Tanvir](https://github.com/Tanvir-yzu)

</div>
