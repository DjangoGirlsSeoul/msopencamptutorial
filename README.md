# Dinewithcode

## Getting Started
	Prerequisites : Python 3.5.x , Git (Windows,Mac), Atom

###### [Installation Instructions](https://github.com/djangogirlscodecamp/msopencamptutorial/blob/master/INSTALL.md)
---
## Fork and Clone this Repository
	a. Click on Fork Button at the top right
<img src="images/fork.png" width="700">

	b. Clone using `git clone https://github.com/<user_name>/msopencamptutorial.git`

<img src="images/clone.png" width="700">

	c. Go inside the folder `cd msopencamptutorial`
	d. Make virtualenv Windows : `C:\Python35\python -m venv myvenv` Mac : `python3 -m venv myvenv` Linux : `virtualenv --python=python3.4 myvenv`
	e. Activate virtualenv Windows: `myvenv\Scripts\activate`  Mac and Linux : `source myvenv/bin.activate` and install requirements `pip install -r requirements`
	f. Create database by running `python manage.py migrate`
	e. Follow below demo from Step 4(b) onwards


# Demo

## Step 1 (Instllation - Setup)
	a. Create gitignore
	b. Install django and create requirements.txt file

## Step 2 (Start Project)
	a. Start Django project

## Step 3 (Basic configuration)
	a. Change settings ( Add `Asia/Seoul` as timezone and set static root `STATIC_ROOT = os.path.join(BASE_DIR, 'static')` )
	b. Setup a database (Use default) then run `python manage.py migrate` to create database. Run server to verify `python manage.py runserver`

## Step 4 (Start app)
	a. Start app rests. Add rests in settings.
	b. Create Restaurant Model with name,address,phone_number,ratings,price,image, and createdAt fields
	c. Create tables for models in your database by running `python manage.py makemigrations rests` and then `python manage.py migrate`

## Step 5 (Django Admin)
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

## Step 12 (Django forms)
	a. Create Django form for adding restaurant
	b. Link template with form and add method in views for saving form
	c. Add Security for form
	d. Add Edit restaurant feature

## Step 13 (Homework)
	a. Implement Sorting based on ratings
	b. Implement Sorting based on restaurant price

## Step 14 (Extended)
