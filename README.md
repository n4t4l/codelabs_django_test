### Clone the Repository:

Open your terminal.

Navigate to the directory where you want to clone the repository and run the command

```
git clone https://github.com/n4t4l/codelabs_django_test.git.
```

Navigate to your project directory 

```
cd codelabs_django_test
```

### Create a Virtual Environment:
Run ```python -m venv venv```

### Activate the Virtual Environment:

On Unix/Linux/macOS, run ```source venv/bin/activate```

On Windows, run ```venv\Scripts\activate```

### Install Requirements:

With the virtual environment activated, run ```pip install -r requirements.txt```

### Run Migrations:

Ensure you're in the project directory  ```cd carrers``` then run ```python manage.py makemigrations``` to create the migrations files (optional but recommended).

Then, run ```python manage.py migrate```. This will create the .sqlite file that will serve as a db for our application.

### Start the Project:

Still in the project directory, run ```python manage.py runserver```
