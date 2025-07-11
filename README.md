# 🏨 Apartmani - Apartment Reservation System

A comprehensive web application for apartment browsing and reservation management. This Django-based system provides an intuitive interface for guests to discover, view, and book apartments with an interactive calendar system.

## 📋 About

Apartmani is a full-featured apartment reservation platform that streamlines the booking process for both guests and property managers. The application features a modern web interface where guests can browse available apartments, view detailed information, and make reservations through an interactive calendar system.

## ✨ Features

### 🏠 **Apartment Management**

- Browse comprehensive apartment listings
- View detailed apartment information including amenities and photos
- Star rating system for apartment quality assessment
- Rich apartment details with descriptions and specifications

### 📅 **Interactive Reservation System**

- Interactive calendar interface for date selection
- Real-time availability checking
- Easy date range selection (check-in to check-out)
- Reservation conflict prevention

### 👥 **Guest Management**

- Guest registration and profile management
- Secure user authentication system
- Guest information storage and management
- Reservation history tracking

### 🔧 **Admin Features**

- Django admin interface for property management
- Apartment, guest, and reservation management
- User role management and permissions
- Comprehensive booking oversight

### 🎨 **Modern UI/UX**

- Responsive design for all devices
- Clean and intuitive user interface
- Modern styling with custom CSS
- User-friendly navigation and forms

## 🛠️ Built With

- **Backend:** Django 4.2+ (Python web framework)
- **Database:** SQLite (development) / PostgreSQL (production ready)
- **Frontend:** HTML5, CSS3, Django Templates
- **Authentication:** Django's built-in authentication system
- **Testing:** Django's testing framework with Factory Boy
- **Development Tools:** Django development server

## 🏗️ Architecture

The application follows Django's Model-View-Template (MVT) architecture with three core models:

- **Apartman** (Apartment): Stores apartment details, amenities, and ratings
- **Gost** (Guest): Manages guest information and user accounts
- **Rezervacija** (Reservation): Handles booking data with relationships:
  - OneToOne relationship with Guest
  - ForeignKey relationship with Apartment

## 🚀 Quick Start

### Prerequisites

- Python 3.8+ (tested with Python 3.13)
- pip (Python package manager)

### Installation & Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/marinactonci/ApartmaniPZW.git
   cd ApartmaniPZW
   ```

2. **Install dependencies**

   ```bash
   pip install "Django>=4.2,<5.0" factory-boy
   ```

3. **Apply database migrations**

   ```bash
   python manage.py migrate
   ```

4. **Create a superuser (for admin access)**

   ```bash
   python manage.py createsuperuser
   ```

5. **Load sample data (optional)**

   ```bash
   python manage.py setup_test_data
   ```

6. **Start the development server**

   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   - Main website: http://127.0.0.1:8000/
   - Admin interface: http://127.0.0.1:8000/admin/

## 📱 Usage

### For Guests:

1. **Browse Apartments**: View available apartments with photos and details
2. **Select Dates**: Use the interactive calendar to choose check-in and check-out dates
3. **Make Reservation**: Fill out the reservation form with your details
4. **Confirmation**: Receive booking confirmation or error messages

### For Administrators:

1. **Access Admin Panel**: Login to `/admin/` with superuser credentials
2. **Manage Apartments**: Add, edit, or remove apartment listings
3. **View Reservations**: Monitor all bookings and guest information
4. **User Management**: Handle guest accounts and permissions

## 🧪 Testing

The application includes comprehensive tests for all models and functionality:

```bash
# Run all tests
python manage.py test

# Run specific model tests
python manage.py test main.tests.test_apartman
python manage.py test main.tests.test_gost
python manage.py test main.tests.test_rezervacija
```

## 📂 Project Structure

```
ApartmaniPZW/
├── main/                   # Main Django app
│   ├── models.py          # Data models (Apartman, Gost, Rezervacija)
│   ├── views.py           # View logic and controllers
│   ├── forms.py           # Django forms for user input
│   ├── urls.py            # URL routing
│   ├── admin.py           # Admin interface configuration
│   ├── tests/             # Test suites
│   ├── static/            # CSS, images, static files
│   ├── management/        # Custom management commands
│   └── migrations/        # Database migrations
├── template/              # HTML templates
│   ├── base_generic.html  # Base template
│   ├── index.html         # Homepage
│   └── main/              # App-specific templates
├── manage.py              # Django management script
├── settings.py            # Django settings
├── urls.py                # Root URL configuration
└── db.sqlite3            # SQLite database (created after setup)
```

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👨‍💻 Credits

**Developed by:**

- **[David Domijan](https://github.com/Specko1903)** - Co-developer
- **[Tonči Marinac](https://github.com/marinactonci)** - Co-developer

---

⭐ **Star this repository if you find it helpful!**
