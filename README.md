# My First Blog
[![Ask DeepWiki](https://devin.ai/assets/askdeepwiki.png)](https://deepwiki.com/mtarek-dev/my-first-blog)

This repository contains the source code for a simple blog application built with Django. It allows users to create, read, update, and delete blog posts, manage drafts, and comment on posts. Authenticated users have additional privileges such as creating and managing posts, and moderating comments.

## Features

*   **User Authentication:** Secure login and logout functionality for users.
*   **Post Management:**
    *   Create new blog posts with a title and text content.
    *   View a list of all published posts.
    *   View individual post details.
    *   Edit existing posts (for authenticated authors).
    *   Delete posts (for authenticated authors).
*   **Draft System:**
    *   Save posts as drafts before publishing.
    *   View a list of drafts (for authenticated users).
    *   Publish drafts to
make them publicly visible.
*   **Commenting System:**
    *   Users can add comments to posts.
    *   Comments require approval by an authenticated user before they are publicly visible.
    *   Authenticated users can approve or remove comments.
*   **Admin Interface:** Django admin interface for managing Posts and Comments (requires superuser access).

## Technology Stack

*   **Backend:** Django
*   **Database:** SQLite (default Django configuration)
*   **Frontend:** HTML, CSS (with Bootstrap for basic styling)

## Setup and Installation

Follow these steps to set up the project locally:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/mtarek-dev/my-first-blog.git
    cd my-first-blog
    ```

2.  **Create and activate a virtual environment (recommended):**
    ```bash
    python -m venv venv
    ```
    *   On Windows:
        ```bash
        venv\Scripts\activate
        ```
    *   On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Apply database migrations:**
    ```bash
    python manage.py migrate
    ```

5.  **Create a superuser (for admin access and post management):**
    ```bash
    python manage.py createsuperuser
    ```
    Follow the prompts to create a username, email (optional), and password.

## Running the Application

1.  **Start the development server:**
    ```bash
    python manage.py runserver
    ```

2.  **Open your web browser and navigate to:**
    *   **Homepage / Post List:** `http://127.0.0.1:8000/`
    *   **Admin Panel:** `http://127.0.0.1:8000/admin/` (login with superuser credentials)
    *   **Login Page:** `http://127.0.0.1:8000/accounts/login/`

## Project Structure

*   `my-first-blog/` (Root project directory)
    *   `manage.py`: Django's command-line utility for administrative tasks.
    *   `requirements.txt`: A list of Python packages required for the project.
    *   `blog/`: The Django application for the blog functionality.
        *   `models.py`: Defines the database models (Post, Comment).
        *   `views.py`: Contains the logic for handling requests and generating responses.
        *   `urls.py`: Defines the URL patterns for the blog app.
        *   `forms.py`: Defines forms for post creation/editing and comments.
        *   `admin.py`: Registers models with the Django admin site.
        *   `templates/`: Contains HTML templates for rendering pages.
            *   `blog/`: Templates specific to the blog app.
            *   `registration/`: Template for the login page.
        *   `static/`: Contains static files (CSS).
        *   `migrations/`: Database migration files.
    *   `mysite/`: The Django project configuration directory.
        *   `settings.py`: Django project settings.
        *   `urls.py`: Root URL configuration for the project.
        *   `wsgi.py`: WSGI entry-point for web servers.
        *   `asgi.py`: ASGI entry-point for web servers.
    *   `db.sqlite3`: The SQLite database file (created after running migrations).
