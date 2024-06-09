# Personal Website

This repository hosts the code for my personal website, a platform to showcase my projects, skills, and achievements. Built using Django, this website features several pages, including a home page and a projects page.

## Table of Contents

1. [Technology Stack](#technology-stack)

2. [Models](#models)

3. [Views](#views)

4. [Templates](#templates)

5. [Installation and Setup](#installation-and-setup)

6. [Progress](#progress)

7. [Future Plans](#future-plans)

## Technology Stack

- Backend: Django
- Frontend: HTML, CSS, Bootstrap
- Database: SQLite (default for Django)
- Other: JavaScript for additional interactivity

## Models

### User

- Fields: username, email, first_name, last_name, is_staff, is_active, date_joined, last_login, permissions
- The User model extends Django's AbstractUser and adds custom fields for user permissions.

## Project

- Fields: name, description, year, link, image
The Project model represents individual projects, with fields for the project name, description, year, link, and image.

## Views

The views for the website are defined using Django's class-based views to handle CRUD operations for projects.

### Home View

Renders the home page.

### Project Views

Handle listing, detail, creation, updating, and deletion of projects.

## Templates

### Base Template (base.html)

The base template includes the main structure of the website including the navbar and footer.

## Home Template (home.html)

The home template extends the base template and includes custom content.

### Installation and Setup

- Intall necessary requirements:

  ```terminal
  pip install -r /path/to/requirements.txt
  ```

- Set up virtual environment:

  ```terminal
  source /path/to/venv/bin/activate
  ```

- Go to the directory where manage.py is located
- Make necessary migrations:

  ```terminal
  python3 manage.py makemigrations
  python3 manage.py migrate
  ```

- Create a superuser:

  ```terminal
  python3 manage.py createsuperuser
  ```

- Add necessary information
- Run the server:

  ```terminal
  python3 manage.py runserver
  ```

- Access the website

```terminal
pip install -r /path/to/requirements.txt
```

- Set up virtual environment:

```terminal
source /path/to/venv/bin/activate
```

-Go to the directory where manage.py is located
-Make necessary migrations:

```terminal
python3 manage.py makemigrations
python3 manage.py migrate
```

-Create a superuser:

```terminal
python3 manage.py createsuperuser
```

-Add necessary information
-Run the server:

```terminal
python3 manage.py runserver
```

-Access the website

## Progress

I have made the following progress on the frontend of my website:

- Navigation bar
- Content for my first page
- Made a basic table
- Included an image in my website

## Future Plans

-Make projects have pop-up windows that explain what they are in more depth
-Make certificates in resume be clickable
-Make a resume page and projects page with working urls
-Style my table to look good
-Beef up content on my homepage to be more appealing
-Write content for my table
-Get images for my projects
-Write my resume and style it
-Have a scroll bar on website
