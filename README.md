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

