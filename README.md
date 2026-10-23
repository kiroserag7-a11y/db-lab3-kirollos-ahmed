# Lab 3: Foreign Keys and Simple SQL

Introduction to Database Systems, Alexandria National University, Faculty of Engineering, Fall 2026.

| Name | ID |
|------|----|
| Kirollos Serag Mouner | 2304102 |
| Ahmed Ramdan Mohamed | 2304109 |

This repository contains Lab 3. The website in `website/` is our **Lab 2 website** (login + to-do list) with the new **Library** pages added (Problem 2). After logging in, use the **Library** link in the top bar.

## Files

| File | Purpose |
|------|---------|
| `problem1_DDL.sql`, `problem1_DML.sql`, `problem1_Answers.txt` | Problem 1 (COMPANY database) |
| `problem2_DDL.sql` | Problem 2: database `library`, tables `author` and `book`, foreign key with `ON DELETE CASCADE` |
| `problem2_DML.sql` | Problem 2: seed data (4 authors, 7 books) |
| `website/` | Lab 2 website + the new library pages |

## How to run it (from an empty machine)

1. Install Python 3.10+ and MySQL Server 8.x.
2. Build the databases (each script drops and recreates its database):
   ```bash
   mysql -u root -p < website/database/schema.sql   # Lab 2: database "registration" (users, todos)
   mysql -u root -p < problem2_DDL.sql              # Lab 3: database "library" (author, book)
   mysql -u root -p < problem2_DML.sql              # Lab 3: seed data
   ```
3. Install the libraries:
   ```bash
   cd website
   python -m venv venv
   # Windows: venv\Scripts\activate      Linux/macOS: source venv/bin/activate
   pip install -r requirements.txt
   ```
4. Copy `.env.example` to `.env` and fill in your MySQL password and a long random `SECRET_KEY`:
   ```bash
   cp .env.example .env        # Windows: copy .env.example .env
   ```
5. Start the server:
   ```bash
   python app.py
   ```
6. Open <http://127.0.0.1:5000>, **register an account**, then click **Library**.

## Library pages (Problem 2)

| ID | Feature | Where |
|----|---------|-------|
| F2.1 | Table of books (with `author_id`) and table of authors | `/library` |
| F2.2 | Add a book / add an author | `Add book`, `Add author` buttons |
| F2.3 | Edit a book / edit an author | `Edit` in each row |
| F2.4 | Remove a book | `Delete` in the books table |
| F2.5 | Remove an author (its books are deleted too, by `ON DELETE CASCADE`) | `Delete` in the authors table |
| Bonus | Cover image for a book, photo for an author | file field in the add/edit forms (saved in `website/static/uploads/`) |

Notes:
- Only simple `SELECT`, `INSERT`, `UPDATE`, `DELETE` statements are used (no JOIN), always with `%s` placeholders.
- The library pages need a logged-in user (same rule as the to-do list).
- The library has its own database, so `website/.env` has an extra line `LIBRARY_DB_NAME=library`.
- Adding a book for an author that does not exist is refused by the foreign key (error 1452) and the page shows "This author does not exist".

## Lab 2 features (unchanged)

Register, login, logout (bcrypt, sessions, CSRF token), private to-do list with add / edit / done / delete, browser and server validation, responsive layout, dark mode. See `website/README.md` for the Lab 2 details and answers.
