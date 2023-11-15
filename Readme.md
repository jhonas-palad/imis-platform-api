# IMIS Cleaning services platform API

## About
This is an API for the our cleaning service platform, which provides a set of endpoints to interact with. The main purpose of this project was to streamline and enhance the user experience for both clients and freelance pro cleaners. By offering a comprehensive set of endpoints, our goal is to empower developers to seamlessly integrate our cleaning service platform into the mobile application interface, allowing for efficient booking, real-time tracking, and robust communication. 

## Note

**Important:** This project is designed to be reusable for future

## Setup

### Local developement

#### Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/jhonas-palad/imis-platform-api.git
   cd your-project
2. Set up your virtual environment
    ```
    python -m venv venv
    ```
    or if you have `virtualenv` on your machine use:
    ```
    virtualenv venv
    ```
    And activate your virtual environment
2. Make sure you have the following installed on your system:

- Python (>=3.10)
- Poetry (Installation guide: https://python-poetry.org/docs/#installation)

    ```
    poetry install
    ```

3. Apply database migrations:
    ```
    python manage.py migrate
    ```
4. Load fixtures:
    ```
    python manage.py loadgeography.py
    ```

5. Run the server:
    ```
    python manage.py runserver
    ```

    Your project should now be up and running locally. Visit http://127.0.0.1:8000/ in your browser to access the development serve