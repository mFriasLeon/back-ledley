
# 🩺 Telemedicine Web App – Ledley

This is the backend of a telemedicine web application named **Ledley**, built with Django and Django REST Framework (DRF). The project is containerized using Docker and uses PostgreSQL as its database. The system is designed to manage users, such as **patients** and **medical professionals**, and enable secure login via JWT tokens.

## 📚 Overview

The goal of this project is to provide a backend API for a modern telemedicine platform. It supports:

- Registration and authentication of users
- Role-based user types (Patients & Professionals)
- Secure password storage
- JWT-based authentication
- FHIR-inspired data modeling
- Docker-based development environment

---

## ⚙️ Tech Stack

- **Python 3.11**
- **Django 4+**
- **Django REST Framework**
- **PostgreSQL**
- **Docker + Docker Compose**
- **Poetry** for dependency management

---

## 🐳 Project Structure

```
.
├── docker-compose.yml         # Docker services definition
├── Dockerfile                 # Django backend container
├── Makefile                   # Useful commands for development
├── manage.py
├── poetry.lock / pyproject.toml
├── README.md
└── src/
    ├── config/                # Django settings and routing
    ├── user/                  # Custom User, Patient, and Professional models
    └── login/                 # Login logic (planned or implemented)
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/ledley-telemedicine.git
cd ledley-telemedicine
```

### 2. Run the app with Docker

```bash
docker compose up --build
```

Or use the Makefile:

```bash
make up
```

### 3. Access the app

- API: [http://localhost:8000](http://localhost:8000)
- PostgreSQL DB: `localhost:5432``

---

## 📦 Makefile Commands

```bash
make up         # Start the containers
make down       # Stop the containers
make shell      # Enter the web container
make clean      # Stop and remove all containers and volumes
make migrate    # Run Django migrations
make superuser  # Create a Django superuser
```

---

## 👤 User Model (FHIR-Inspired)

The system is inspired by the [FHIR](https://www.hl7.org/fhir/) specification. The base `User` model includes:

- `id`
- `username`
- `name`
- `gender`
- `birth_date`
- `email`
- `active`
- `created_date`

Extended via one-to-one relationships:

- `Patient`
- `Professional` (with `role`)

Each is uniquely linked to a `User`.

---

## 🔐 Authentication

Authentication is handled using **JWT** via the `djangorestframework-simplejwt` package.

### Features:

- Encrypted password handling using Django utilities
- Token generation and login via `/api/token/`
- Token refreshing via `/api/token/refresh/`
- Secure login view to validate credentials

---

## 🧪 Development Tips

To create a new Django app:

```bash
make shell
python manage.py startapp your_app_name
```

To run migrations:

```bash
make migrate
```

To create a superuser:

```bash
make superuser
```

---

## 📌 Planned Features

- Appointment scheduling
- Video consultations (via WebRTC or external provider)
- Notifications system (SMS/email)
- Admin dashboard for clinical staff
- FHIR import/export support

---



## 👨‍⚕️ Author

**Manuel Frías León**