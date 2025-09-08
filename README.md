# CatchARide

CatchARide is a simple Django web application for managing cars. The project was built as a practice CRUD (Create, Read, Update, Delete) app to understand how Django models, views, templates, and static files work together.

---

## Description

The app allows users to add cars, view a list of all cars, see detailed information about a specific car, update existing cars, and delete cars. The frontend uses Django templates and custom CSS for styling, while the backend is powered by Django’s ORM and generic class-based views. The project structure includes separate templates for each page (home, about, car index, car detail, forms, and delete confirmation) and organized static files for styling.

---

## Functionality

- **Home Page**: Landing page for the application.  
- **About Page**: Provides information about the app.  
- **View Cars**: Displays all cars in a list view.  
- **Car Detail**: Shows detailed information about a single car.  
- **Add Car**: Form to add a new car to the database.  
- **Update Car**: Form to edit details of an existing car.  
- **Delete Car**: Confirmation page to remove a car.  
- **Admin Panel**: Cars are also managed through the Django admin site.  

---

## Technology Used

- **Django** (Python framework for backend and templates)  
- **Django ORM** (database management, default SQLite)  
- **HTML5 & Django Templates** (frontend structure)  
- **CSS3** (custom styles for layout and pages)  
- **Pipenv** (virtual environment and dependency management)  

---

## Project Highlights

- Full CRUD functionality for car management.  
- Clean project structure with separate apps, templates, and static files.  
- Base template with navigation, extended by all pages.  
- Dedicated CSS files for home, forms, car index, and car detail views.  
- Designed for learning Django fundamentals with practical implementation.  

---

## License

This project is created for educational purposes and is not intended for production use.


## Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/your-username/catcharide.git
cd catcharide

pipenv install
pipenv shell

python manage.py migrate

python manage.py runserver

http://127.0.0.1:8000/


Current files tree
my_app/
 ┣ migrations/
 ┣ templates/
 ┃ ┣ main_app/
 ┃ ┃ ┣ car_form.html
 ┃ ┃ ┗ car_confirm_delete.html
 ┃ ┣ cars/
 ┃ ┃ ┣ index.html
 ┃ ┃ ┗ detail.html
 ┃ ┣ home.html
 ┃ ┣ about.html
 ┃ ┗ base.html
 ┣ static/
 ┃ ┗ css/
 ┃   ┣ base.css
 ┃   ┣ home.css
 ┃   ┣ form.css
 ┃   ┗ cars/
 ┃       ┣ car-index.css
 ┃       ┗ car-detail.css
 ┣ models.py
 ┣ views.py
 ┣ urls.py
 ┗ ...
```
