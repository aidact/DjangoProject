# My_food

Have you ever wondered are this products compatible? Or how many nutrients does dumpling contain? 

Then this app is for you. My_food is a mobile app for tracking calories, carbs and proteins in every meal and water balance during the day. This app helps to create more balanced diet with all products needed to user. It gives feedback after every day and shows statistics. 

The project is written on python Django (DRF). 

Follow steps below to install and test project:
1. Clone the repo
```
git clone https://github.com/aidact/DjangoProject.git
```
2. Create an environment
```
virtualenv env
```
3. Activate the environment

Unix based System
```
source env/bin/activate
```
Windows
```
env\Scripts\activate
```
4. Install required libraries
```
pip install -r requirements.txt
```
4. Create a file .env and write necessary things 
5. Create tables in the database:
```
python manage.py migrate
```
6. Run the project
```
python manage.py runserver
```
or 
```
./manage.py runserver
```
