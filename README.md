# MASTER BLOG Flask MVVM CRUD Application

## 📌 Project Overview
This project is a **Flask-based web application** following the **MVVM (Model-View-ViewModel) pattern** with **CRUD (Create, Read, Update, Delete) operations** for blog management. It uses **Jinja2 templates** for rendering dynamic content.

## 📂 Folder Structure
```
Masterblog/
│── app.py                  # Main application entry point
│── config.py               # Configuration settings
│── requirements.txt        # Dependencies
│── LICENSE                 # License file
│── README.md               # Project documentation
│
├── data/
│   ├── blogs.json          # JSON-based data storage for blogs
│
├── helpers/
│   ├── json_file_helper.py # Helper functions for reading/writing JSON
│   ├── print_helper.py     # Debugging print helpers
│
├── models/
│   ├── blog_model.py       # Data model for blog posts
│
├── viewmodels/
│   ├── blog_view_model.py  # ViewModel for handling business logic
│
├── views/
│   ├── app_view.py         # Main application views
│   ├── blog_view.py        # Blog CRUD views
│
├── templates/
│   ├── index.html          # Homepage template
│   ├── add.html            # Add blog template
│   ├── update.html         # Update blog template
│
├── static/
│   ├── style.css           # Styling for the frontend
```

---

## 🔧 Setup Instructions

### 1️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 2️⃣ Run the Flask Application
```bash
python app.py
```

### 3️⃣ Open the Application in Browser
Navigate to:
```
http://127.0.0.1:5000/
```

---

## 🎯 Understanding MVVM Architecture in Flask

MVVM (Model-View-ViewModel) pattern helps in **separating concerns** between:

- **Model** → Handles data logic (e.g., `blog_model.py`)
- **View** → Manages UI rendering using Jinja templates (e.g., `index.html`)
- **ViewModel** → Manages business logic between the view and model (e.g., `blog_view_model.py`)

### 🛠 CRUD Operations

| Operation | Route | Description |
|-----------|----------------------|------------------------------|
| **Create** | `POST /add` | Adds a new blog post |
| **Read** | `GET /` | Lists all blog posts |
| **Update** | `POST /update/<id>` | Updates a blog post |
| **Delete** | `POST /delete/<id>` | Deletes a blog post |

### ✍ **Example Blog JSON Format**
```json
{
  "blog_id": 1,
  "title": "Flask MVVM Explained",
  "author": "John Doe",
  "content": "This post explains MVVM in Flask.",
  "likes": 5
}
```

---

## 💡 Key Features
✅ **Flask with Jinja Templates** for UI rendering  
✅ **CRUD Operations** with JSON file storage  
✅ **MVVM Pattern** for structured code  
✅ **Modularized Codebase** with Helpers, Models, and Views  

---

## ⚡ Future Enhancements
- 🔹 **Move from JSON storage to SQL database**
- 🔹 **Add user authentication**
- 🔹 **AJAX for better UI experience**

---

## 📜 License
This project is licensed under the MIT License. Feel free to use and modify it!
