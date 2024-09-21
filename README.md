# Vakil Desk Assignment
## Project Setup
for project setup perform the following steps,
1. Create a Python virtual environment.
2. Clone the project by executing the following command:
   ```bash
   git clone https://github.com/urbuddy/Simple-Admin-dashboard.git
   ```
3. Install the requirements:
```bash
pip install -r requirements.txt
```
4.1. For the first two and last 3 questions' solutions you can see and run the following files  
      i. que1sol.py  
      ii. que2sol.py  
      iv. que4sol.py  
      v. que5sol.py  
      vi. que6sol.py  
  command to execute the file:  
  ```bash
  python {file_name.py}
  ```
  2. For the 3rd question solution you have to see the project top_customer_display and set it up as follows to see the result.  
       i. Migrate the migration files
       ```bash
       python manage.py migrate
       ```
       ii. Create a super user(admin)
       ```bash
       python manage.py createsuperuser
       ```
       iii. run server
       ```bash
       python manage.py runserver
       ```
       iii. create the users and orders from the admin site using the following URL by logging in with superuser credentials
       ```bash
       http://127.0.0.1:8000/admin/
       ```
       iv. see the result in the following URL
       ```bash
       http://127.0.0.1:8000/
       ```
       
