
# ✅ Todo List API Base

A simple RESTful API built with Django REST Framework to manage a todo list. This project is a basic starter template for building APIs with authentication and CRUD operations.

---

## 🚀 Features

- Create, read, update, and delete (CRUD) todo items  
- User authentication (token or session based)  
- Simple and clean API endpoints  
- Built with Django REST Framework  

---

## 🧰 Tech Stack

- Python 3.x  
- Django 5.x  
- Django REST Framework (DRF)  

---

## ⚙️ Installation and Setup

1. Clone the repo:

```bash
git clone https://github.com/Rezanikmanesh-79/todo_list_api_base.git
cd todo_list_api_base
````

2. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate     # Linux/macOS
venv\Scripts\activate        # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Apply migrations:

```bash
python manage.py migrate
```

5. Create a superuser:

```bash
python manage.py createsuperuser
```

6. Run the development server:

```bash
python manage.py runserver
```

---

## 📡 API Endpoints

| Method | Endpoint           | Description          |
| ------ | ------------------ | -------------------- |
| GET    | `/api/todos/`      | List all todo items  |
| POST   | `/api/todos/`      | Create a new todo    |
| GET    | `/api/todos/<id>/` | Retrieve a todo item |
| PUT    | `/api/todos/<id>/` | Update a todo item   |
| DELETE | `/api/todos/<id>/` | Delete a todo item   |

---

## 👨‍💻 Author

**Reza Nikmanesh**
GitHub: [@Rezanikmanesh-79](https://github.com/Rezanikmanesh-79)

---

## 📝 License

MIT License — free for personal and educational use.


