# FlaskSchool 🏫

A **Flask-based web application** designed to manage school operations.  
It provides full **CRUD (Create, Read, Update, Delete)** functionality for **Teachers, Students, and Staff**.  
This project is similar to the Django-based school management system but built using Flask and related modules.  

---

## 🚀 Features
- Manage **Teachers**, **Students**, and **Staff** with full CRUD support  
- Simple and responsive web interface  
- Uses Flask’s lightweight architecture for fast development  
- Modular design with templates and static files separation  
- Easy to extend with additional modules  

---

## ⚙️ Installation & Setup

### Clone the repository
```bash
git clone https://github.com/yourusername/FlaskSchool.git
cd FlaskSchool
```
### 1. Install Flask
```bash
pip install flask
```
### 2. Create Virtual Environment (Windows)
```bash
python -m venv venv
.\venv\Scripts\activate
```
(For Linux/Mac:)
```bash
python3 -m venv venv
source venv/bin/activate
```
### 3. Install Requirements
```bash
pip install -r requirements.txt
```
### 4. Run the Flask Project
```bash
set FLASK_ENV=development
flask run
```
Eg;
```bash
set FLASK_APP=school.py
flask run
```
