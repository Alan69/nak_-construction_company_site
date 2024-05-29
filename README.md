# NAK Construction Company Website

## Overview

This project is a web application for the NAK Construction Company, designed to showcase the company's projects and services. The website provides detailed information about the company's offerings and enables potential clients to easily get in touch. It is built using Django, SQLite, HTML, CSS, JavaScript, and Bootstrap.

## Features

- **Project Portfolio**: Display a comprehensive list of the company's construction projects.
- **Service Listings**: Detailed information about the services provided by NAK.
- **Contact Form**: Users can send inquiries directly through the website.
- **Responsive Design**: Optimized for viewing on various devices using Bootstrap.
- **Secure Authentication**: User login and registration system with Django's built-in authentication.

## Technologies Used

- **Backend**: Django
- **Database**: SQLite
- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **Version Control**: Git

## Installation

### Prerequisites

- Python 3.x
- pip (Python package installer)
- Git

### Steps

1. **Clone the repository**:
    ```bash
    git clone https://github.com/Alan69/nak-construction-website.git
    cd nak-construction-website
    ```

2. **Create a virtual environment**:
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Apply migrations**:
    ```bash
    python manage.py migrate
    ```

5. **Create a superuser**:
    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server**:
    ```bash
    python manage.py runserver
    ```

7. **Open the website**:
    Open your web browser and go to `http://127.0.0.1:8000`

## Configuration

### Database

The project uses SQLite by default. For production use, it's recommended to switch to a more robust database system like PostgreSQL. Update the `DATABASES` setting in `settings.py` accordingly.

### Static Files

For production, configure the static files storage using a service like AWS S3 or Google Cloud Storage. Update the `STATIC_URL` and `STATICFILES_STORAGE` settings in `settings.py`.

## Deployment

### Using Heroku

1. **Install the Heroku CLI**: Follow instructions from [Heroku](https://devcenter.heroku.com/articles/heroku-cli).

2. **Create a new Heroku app**:
    ```bash
    heroku create
    ```

3. **Deploy the app**:
    ```bash
    git push heroku main
    ```

4. **Run migrations on Heroku**:
    ```bash
    heroku run python manage.py migrate
    ```

5. **Open the deployed app**:
    ```bash
    heroku open
    ```

### Other Hosting Providers

Refer to the specific documentation of your hosting provider for deploying Django applications.

## Contributing

1. **Fork the repository**.
2. **Create a new branch**:
    ```bash
    git checkout -b feature-branch
    ```
3. **Make your changes and commit them**:
    ```bash
    git commit -m "Description of changes"
    ```
4. **Push to the branch**:
    ```bash
    git push origin feature-branch
    ```
5. **Create a Pull Request**.

## Acknowledgments

- Special thanks to the Django, Bootstrap, and all other open-source projects that made this project possible.
