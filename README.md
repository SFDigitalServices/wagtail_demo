# Coding Challenge - Wagtail

Repository for the coding challenge.

## Prompt

### Backstory

At the company Widgets and More, we pride ourselves making the best widgets in the industry and for all your widgety needs. However, in this day and age, one needs a digital presence in order to get the word out about our wonderful widgets, any information and documentation regarding said widgets, and ways to interact with our widget-buying customers and clients.

With a launch of the newest and shiniest Widget, yet, we need to get the news out there and need a new type of page in our content management system (CMS).

### Task at Hand

Time Limit: 90 minutes

Requirements:

* Create a `WidgetDocumentation` within the Wagtail CMS. This page type should be able to handle a title, description, and body content as rich text.

* Since the documentation page can become rather long, we'll want a table of contents at the top of the page that can deeplink to the different major sections/headings


### Install Conda

We recommend using the miniconda but virtual environments or  anything with a working pip and python 3.9 should work.

### Create and activate the Conda environment

If you're not there already, go to the directory where you cloned this project and then run the following commands:

```sh
conda env create -f=requirements/conda_env.yml
conda activate wagtail_demo
```

### Install Python requirements

```sh
pip install -r requirements/app.txt
```

### Bootstrap the database and super user account

Next you'll run [Django's][django] `manage.py` to initialize the database and create the super user account:

```sh
./manage.py migrate
./manage.py createsuperuser
```

Follow the prompts. Your password will only be used for local access, so don't worry about making it secure.

### Running Tests

```sh
pytest
```
### Start the server

Start the [Django] [development server](https://docs.djangoproject.com/en/4.1/ref/django-admin/#runserver) with `manage.py`:

```sh
./manage.py runserver
```

