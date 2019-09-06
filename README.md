# Learning Django

# Project Requirements
1. Python 3
2. Pip
4. PostgreSQL
5. pgAdmin (Optional)
6. psycopg2 (if not install in your local environment)

    `sudo apt-get install python3-Psycopg2`
    
    1. if pip not install
    
        ` sudo apt-get install python3-pip`
    
    2. Now you can install Psycopg2 using pip3
    
        `sudo pip3 install Psycopg2`
    
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
 6. Add pusher credentials in environment file
    
    `PUSHER_APP_ID`
    `PUSHER_APP_KEY`
    `PUSHER_APP_SECRET`
    `PUSHER_APP_CLUSTER`

# Finally production host with server
 1. Production server is ready with apache2
 2. apache2 config file in production directory
 3. `production/apache config.conf` replace with `/etc/apache2/sites-available/000-default.conf`