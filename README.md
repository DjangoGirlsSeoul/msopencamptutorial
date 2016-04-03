# Dinewithcode

## Step 1
	a. Create gitignore
	b. Install django and create requirements.txt file

## Step 2
	a. Start Django project

## Step 3
	a. Change settings ( Add `Asia/Seoul` as timezone and set static root `STATIC_ROOT = os.path.join(BASE_DIR, 'static')` )
	b. Setup a database (Use default) then run `python manage.py migrate` to create database. Run server to verify `python manage.py runserver`

## Step 4
	a. Start app rests. Add rests in settings.
	b. Create Restaurant Model
	c. Create tables for models in your database by running `python manage.py makemigrations rests` and then `python manage.py migrate`

## Step 5
	a. Django Admin - Add your model to admin.py
	b. Create Superuser and test your model from admin interface

## Step 6 (Deploy)
	a. Create a free account on PythonAnywhere.com and pulling our code there
	b. Create Virtualenvironment on PythonAnywhere `virtualenv --python=python3.4 myvenv` and install requirements using `pip install -r requirements.txt`
	c. Creating the database on PythonAnywhere by running `python manage.py migrate`
	d. Publishing our site as web app - set virtualenv and wsgi file

## Step 7 (Django Urls)
	a. Add Django url to point home page to restaurant list

## Step 8 (Django Views)
	a. Create first view function in views.py

## Step 9 (Django Template)
 	a. Create Template for rest list with dummy data using bootstrap
	b. Create Template for restaurant detail page
	c. Create base template and extend list and detail template from it

## Step 10 (Dynamic Data in Template with Django ORM)
	a. Get Dynamic data (restaurants) from database using queryset
	b. Populate rest list template with dynamic data

## Step 11 (Extend application)
	a. Show Restaurant detail page with dynamic data
	b. Deploy to PythonAnywhere with `python manage.py collectstatic`
