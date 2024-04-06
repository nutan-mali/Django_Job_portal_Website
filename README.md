#Django Job Portal Website


This project is a Django-based job portal website with a single sign-up and login page. Users can choose between employer and job seeker roles using radio buttons during the sign-up process. Once logged in, users will have access to role-specific functionalities.

Sign-up and Login

Sign-up Page: Users can sign up by providing their email, password, and selecting their role (employer or job seeker) using radio buttons.

Login Page: Authenticated users can log in with their credentials.
User Roles

Employer: Users with the employer role can post, read, edit, and delete job listings.

Job Seeker: Users with the job seeker role can apply for jobs, upload resumes, and view details of applied jobs.
Radio Buttons for Role Selection

During the sign-up process, users are presented with radio buttons to choose their role:

Employer Radio Button: Selecting this option indicates that the user wants to sign up as an employer.

Job Seeker Radio Button: Selecting this option indicates that the user wants to sign up as a job seeker.
Project Structure

The project follows a standard Django application structure with models, views, templates, and URLs organized based on user roles (employer and job seeker). The single sign-up and login page dynamically handles user role selection using radio buttons.

Getting Started
To run the project locally:

Clone the repository to your local machine.
Install Python and Django if not already installed.
Set up a virtual environment for the project.
Install project dependencies using pip install -r requirements.txt.
Run database migrations using python manage.py migrate.
Start the development server with python manage.py runserver.
Access the website and navigate to the sign-up page to create an account by selecting the desired role using radio buttons.
