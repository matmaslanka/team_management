# Team management
An application based on Django to manage team tasks. The user can add employees, create tasks with their status, and assign existing tasks to employees.

## Installation

1. Clone the repository:
   `git clone https://github.com/matmaslanka/team_management.git`
2. Set up a virtual environment:
   python3 -m venv env <br/>
   source env/bin/activate  # On Windows: env\Scripts\activate
3. Install the dependencies from requirements.txt:
   `pip install -r requirements.txt`
4.  Open a terminal and navigate to the project directory in bash: 
   `cd .\team_management`
5. Add your own secret key to `team_management\settings.py` on line 24.
   Example: "0ne2fxv8vpeisxbd1xtq2kx-vnlv_7bnf%8nwc+jj(bpoe3_@v"
   (Note: The secret key is hidden for security reasons.)
6. Set up the database and run migrations (the application will crash without this step):
   `python manage.py migrate`

## Running the project
1. Run the Django development server:
   `python manage.py runserver`
2. Access the project in your browser at: http://127.0.0.1:8000/.

## Usage

When the user runs the application, they will see a homepage. The navigation bar contains a single tab labeled "Home," which takes the user back to the starting page. The first step is for the user to create an employee by clicking the designated button. After clicking it, a form will appear. The user must fill out the form by providing employee details such as first name, last name, description, position, and an optional task.

The user can also create a task by clicking the button on the homepage. After clicking, they must fill out the form by adding a title, description, and status.

Once an employee is added, the user will see a list of employees displayed on the homepage. By clicking on a specific employee, the user can add new tasks and update existing tasks.

### Admin Access
(Optional) To access the Django admin interface, create a superuser account:
   `python manage.py createsuperuser`
