# Learning Django

# Project Requirements
1. Python 3
2. Pip
3. Web Server (Ex. Apache, Ngnix)
4. PostgreSQL
5. pgAdmin (Optional)

# Project Setup
1. Clone this project using this command below:

    `https://github.com/mkawsar/django.git`
2. Install project dependencies

    `pip install -r requirements.txt`
3. Copy environment file
    
    `cp .env.example .env` (Using Ubuntu CLI)
    
    Then added database information in `.env` file.
    
 4. Creating project tables migration
    
    `python3 manage.py migrate`
 5. Finally run project
 
    `python3 manage.py runserver`