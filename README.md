# TODO MANAGEMENT APPLICATION
This is a Todo Management application built with
- python
- django
- javascript
- MySQL

# How to setup
Follow these steps to set up the project on your local machine


### clone the Repository
```bash
git clone https://github.com/JainMariyam/todohome_challenge.git
cd-todo_challenge
```

### Backend setup

- Create virtual environment
  
  ```bash
  python -m venv env
  ```

- Activate the virtual environment
 
   ```bash
  env\Scripts\activate.bat
  ```

  ### Required Modules

- Django
- requests
- markdown

   ```bash
  pip install django requests markdown
  ```

 - Run database migration:

 ```bash
  python manage.py migrate
  ```

 - Start the Django development server:

 ```bash
  python manage.py runserver
  ```

### Database setup
1. Create a new database in MySQL or any other relational database of your choice.
2. Update the database configuration in settings.py
3. Run the database migrations

```bash
  python manage.py migrate
  ```
 
## Access the Application

You can now access the application by visiting http://localhost:8000/ in your web browser.
