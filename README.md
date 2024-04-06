# Django Job Portal Website
This Django-based job portal website offers a streamlined experience for both employers and job seekers, featuring a user-friendly interface and role-specific functionalities.

# Features
# User Roles
Employer: Post, read, edit, and delete job listings.

Job Seeker: Apply for jobs, upload resumes, and manage applications.

# Sign-up and Login

Sign-up Page: Register with email, password, and choose role (employer or job seeker) using radio buttons.

Login Page: Secure access for authenticated users.

Role Selection

During sign-up, users select their role using radio buttons:


Employer Radio Button: Register as an employer.

Job Seeker Radio Button: Register as a job seeker.

# Project Structure

The project adheres to Django's standard structure:

Models: Define data models for users, jobs, applications, etc.

Views: Handle user requests, render templates, and manage logic.

Templates: HTML templates for user interface design.

URLs: Routing URLs to corresponding views.

# Getting Started

Clone Repository: Get the project code on your local machine.

Install Dependencies: Install Python, Django, and project dependencies using pip.

Setup Virtual Environment: Isolate project dependencies using a virtual environment.

Database Setup: Run database migrations to create necessary tables.

Run Development Server: Start the Django development server to preview the website.

Access the Website: Navigate to the sign-up page, select your role, and create an account to explore the functionalities.
Setup Instructions


Copy code
# Clone the repository
git clone <https://github.com/nutan-mali/Job_portal>

cd project_folder

# Install dependencies
pip install -r requirements.txt

# Run database migrations
python manage.py migrate

# Start development server
python manage.py runserver

Additional Notes
Customize templates and stylesheets for a personalized look.
Implement additional features like job search, notifications, and user profiles as needed.


# URL Patterns

# Admin Panel
URL: /admin/

Description: Default URL for accessing the Django admin panel.

# Home Page
URL: /

Description: Homepage URL linked to the views.index function to display the home page.

# Sign-up Page
URL: /signup/

Description: URL for the sign-up page linked to the views.signup function.

# Login Page
URL: /login/

Description: URL for the login page linked to the views.login function.



# Employer Page
URL: /employer/

Description: URL for employer-specific functionality linked to the views.employer function.


# Job Seeker Page
URL: /job_seeker/

Description: URL for job seeker-specific functionality linked to the views.job_seeker function.
