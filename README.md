# Flask CRUD Operation

A simple **Flask** web application demonstrating basic **CRUD** (Create, Read, Update, Delete) operations using Flask, SQLAlchemy, and SQLite.

Perfect as a beginner-friendly reference or starting point for learning Flask database integration and form handling.

## Features

- Create new records
- View all records in a list
- Update existing records
- Delete records
- Basic form validation & user feedback (success/error messages)
- Clean Jinja2 templating

## Technologies Used

- **Python** 3.x
- **Flask** – web framework
- **Flask-SQLAlchemy** – ORM for database operations
- **SQLite** – lightweight database (default)
- **Jinja2** – templating engine
- **HTML** + **Bootstrap** (optional – if used in templates)

## Project Structure
  Flask-CRUD-Operation/
├── app.py              # Main Flask application + routes
├── models.py           # SQLAlchemy model definitions
├── templates/          # HTML templates
│   ├── base.html       # Base layout
│   ├── index.html      # List all records
│   ├── create.html     # Create form
│   ├── update.html     # Edit form
│   └── ...             # Possibly other partials
├── .gitignore
└── LICENSE


## Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/erenomar-sw/Flask-CRUD-Operation.git
cd Flask-CRUD-Operation
```
### 2. Create virtual environment (recommended)

# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate

### 3. Install dependencies
pip install flask flask-sqlalchemy

### 4. Run the application
Bashpython app.py
# or
flask run

## Usage

- Open the home page → see list of all items
- Click **"Add New"** → fill the form → submit
- Click **Edit** on any item → modify → save
- Click **Delete** to remove an item

## Future Improvements (Ideas)

- Add WTForms + Flask-WTF for better form handling & CSRF protection
- Use Bootstrap or Tailwind for nicer UI
- Add search/filter functionality
- Implement login & user-specific records
- Add data validation & error handling improvements
- Deploy to Render, Railway, Heroku, etc.


## License

This project is licensed under the MIT License — feel free to use it for learning or your own projects.


