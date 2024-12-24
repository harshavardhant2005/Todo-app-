# To-Do App with Python Flask and SQLite

## Overview
This is a simple yet functional To-Do application built using the Python Flask framework and SQLite database. The app provides a clean and intuitive user interface for managing tasks, enabling users to create, view, update, and delete tasks effortlessly. It is a great example of a CRUD (Create, Read, Update, Delete) application designed for learning or small-scale task management.

## Features
- **Task Management**:
  - Add new tasks with titles and optional descriptions.
  - View a list of all tasks with their current statuses.
  - Update task details or mark tasks as completed.
  - Delete tasks no longer needed.
- **Database Integration**:
  - Uses SQLite for persistent data storage.
  - Automatically creates the database file on the first run.
- **User-Friendly Design**:
  - Clean and responsive user interface for easy navigation.
  - Simple and minimalistic design to focus on functionality.
- **Lightweight**:
  - Built with Flask, a lightweight and flexible Python framework.
  - Suitable for deployment on small servers or personal projects.

## Technologies Used
- **Backend**: Python with Flask
  - Flask is a lightweight WSGI web application framework in Python. It is designed with simplicity and flexibility in mind, making it ideal for building small and scalable web applications. Flask handles routing, request handling, and templating in this project.

- **Frontend**: HTML, CSS 

- **Database**: SQLite
  - SQLite is a self-contained, high-reliability, embedded, SQL database engine. It requires no setup or server and stores data in a single file. In this project, SQLite initializes the database structure and ensures persistent task storage.

- **Tools**: Jinja2 for templating

## Installation and Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/harshavardhant2005/Todo-app-.git
   cd todo-app
   ```

2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Windows: venv\Scripts\activate
   pip install flask
   ```

3. Initialize the SQLite database:
   - Ensure the `Todo.db` file is created by running the Flask app for the first time. The app contains code to automatically initialize the database schema if it does not exist.

4. Run the application:
   ```bash
   python app.py
   ```
  After initializing the server, click on the running server link to open the application.

## Screenshots
![Screenshot 2024-12-24 204532](https://github.com/user-attachments/assets/9bc7977d-7086-4425-a473-aaddaec4f6f5)
![Screenshot 2024-12-24 204548](https://github.com/user-attachments/assets/63242811-ce09-490d-96df-6e72fe181203)



## Contribution
Feel free to fork this repository, make improvements, and submit pull requests. Suggestions and feedback are always welcome!


