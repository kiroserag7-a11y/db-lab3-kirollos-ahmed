# Lab 2: Login & To-Do Application

Introduction to Database Systems, Alexandria National University, Faculty of Engineering, Fall 2026.

## 1. Team

| Name | ID | Who did what |
|------|----|--------------|
| Kirollos Serag Mouner | 2304102 | Database (`schema.sql`), Flask back end, sessions, bcrypt, server-side validation |
| Ahmed Ramdan Mohamed | 2304109 | HTML templates, CSS (responsive, dark mode), JavaScript validation, README, testing |

## 2. Technology

- **Back end:** Python 3 + Flask (sessions, Jinja templates), `bcrypt` for hashing, `PyMySQL` with `%s` placeholders (plain SQL, no ORM)
- **Front end:** HTML, plain CSS (flexbox/grid, media query for phones), vanilla JavaScript
- **Database:** MySQL, database `registration`, tables `users` and `todos`

## 3. How to run it (from an empty machine)

1. Install Python 3.10+ and MySQL Server 8.x.
2. Get the code and install the libraries:
   ```bash
   git clone <repository-url>
   cd db-lab2-kirollos-ahmed
   python -m venv venv
   # Windows: venv\Scripts\activate      Linux/macOS: source venv/bin/activate
   pip install -r requirements.txt
   ```
3. Build the database (this drops and recreates `registration`):
   ```bash
   mysql -u root -p < database/schema.sql
   ```
4. Copy `.env.example` to `.env` and fill in your MySQL password and a long random `SECRET_KEY`:
   ```bash
   cp .env.example .env        # Windows: copy .env.example .env
   ```
5. Start the server:
   ```bash
   python app.py
   ```
6. Open <http://127.0.0.1:5000> in the browser.

## 4. Features

| # | Feature | Done |
|---|---------|------|
| R1 | Register (name, e-mail, password, confirm). Duplicate e-mail shows `Email Already Exists`. User is logged in afterwards. | yes |
| R2 | Login, same `Invalid email or password` for wrong e-mail and wrong password, Logout destroys the session. | yes |
| R3 | Private list: not logged in means redirect to login; each user sees only their own to-dos, newest first. | yes |
| R4 | Add a to-do | yes |
| R5 | Edit the title | yes |
| R6 | Mark done / not done | yes |
| R7 | Delete with an "are you sure?" confirmation | yes |
| R8 | Checks in the browser (JavaScript) and again on the server, with the exact messages | yes |
| R9 | bcrypt hashes, only the given queries, always parameterized, `user_id` taken from the session | yes |
| R10 | Consistent, responsive UI (works at 360 px), feedback messages, done state, empty state, styled error pages | yes |

**Bonus:** count of open/done to-dos, filter (all / open / done), dark mode (follows the system setting).

Extra safety not asked for: CSRF token on every POST form, length checks that match the column sizes (name 100, e-mail 255), and a password limit of 72 bytes (bcrypt's limit).

## 5. Screenshots

Put the four screenshots in the `screenshots/` folder with these names:

![Register page with errors](screenshots/register-errors.png)
![Login page](screenshots/login.png)
![To-do list with a done item](screenshots/list.png)
![Phone-sized window](screenshots/phone.png)

## 6. Answers

**(a) Why do `UPDATE` and `DELETE` contain `AND user_id = ?`, and what changes if you remove it?**
The `todo_id` comes from the browser, so anyone can send another user's number. `AND user_id = ?` uses the id of the logged-in user (from the session), so for a to-do that is not yours the statement changes zero rows. Without it, any logged-in user could edit, mark or delete other people's to-dos just by changing the number in the request.

**(b) What happens if you insert a to-do for a `user_id` that does not exist, and which constraint is that?**
MySQL refuses the insert with error 1452 (a foreign key constraint fails). This is the **foreign key constraint**, which enforces **referential integrity**: every `todos.user_id` must match an existing `users.user_id`.

**(c) Why do you store a hash and not the password?**
If the database leaks, the attacker gets only hashes and not the real passwords (which many people reuse on other sites). bcrypt is one-way, adds a random salt (equal passwords give different hashes) and is slow on purpose, which makes guessing very expensive. Even the administrators cannot read the passwords.

**(d) The `name` column is `NOT NULL`: why do we still need our own check for an empty name?**
`NOT NULL` only refuses the value `NULL`. An empty text `''` (or only spaces) is a real value, so MySQL accepts it. Only our own check, in the browser and on the server, can refuse an empty name.

## Project structure

```
db-lab2-kirollos-ahmed/
  README.md
  .gitignore            # lists .env
  .env.example          # fake values only
  requirements.txt
  app.py                # Flask server
  database/schema.sql   # both tables, re-runnable, no data
  templates/            # Jinja pages
  static/               # style.css, app.js
  screenshots/
```
