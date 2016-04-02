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