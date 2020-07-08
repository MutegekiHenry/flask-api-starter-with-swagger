#  Reusable Flask Starter Project API
Flask wrapper REST Api project. This project is aimed at creating a flask structure that is reusable for any flask project. All you have to do is just clone/fork, customise db details and start building your API in the less than 5minutes. This project uses the following technologies: 

1. `Flask`
2. `Swagger` 
3. `SQLAlchemy`


### Project Setup

Follow these steps to have a local running copy of the app.

##### Clone The Repo

`git clone <url-to-repo>`

If `master` is not up to date, `git checkout develop`. However, note that code on develop could be having some minor issues to sort.

##### Install PostgreSQL

Here's a great resource to check out:

[How To Install and Use PostgreSQL](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-18-04)

Create a development database and call it `dev_db`.

##### Create a Virtual Environment

create virtual enviroment called venv

Run `virtualenv venv`

##### Activate the virtual environment.

Run `. venv/bin/activate`

Make sure you have `pip` installed on your machine.

##### Install the dependencies.

`pip install -r requirements.txt`

##### Create a .env file
Create a `.env` file (which defines the environment variables used) at the root of the app.

Add the following details, customizing as needed.

```
export FLASK_APP=server.py
export FLASK_ENV=development
export FLASK_RUN_PORT=5000
```
##### Run Database migrations
 
Run migrations for the database

`python manage.py db upgrade`

##### Run Application
 
Run the application with this command

`flask run`

##### Test the API

Through your browser go to link `localhost:<flask_port>/`.


##### Checkout Api docs

Through your browser go to link `localhost:<flask_port>/apidocs`.
