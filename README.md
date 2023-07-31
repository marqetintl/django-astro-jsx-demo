# django-astro-demo

This is a demo illustrating how to use [Astro](https://astro.build) with [Django](https://www.djangoproject.com/).

## Installation

1. Once in your work directory, clone this repo and navigate to it:

```bash
git clone https://github.com/marqetintl/django-astro-jsx-demo.git
cd django-astro-jsx-demo
```

2. Install python and node dependencies.

Run the following commands:

```bash
python3 -m venv env
. env/bin/activate
cd django
pip3 install -r requirements.txt
python3 manage.py runserver
```

Open a new terminal:

```bash
cd astro
yarn
yarn watch
```

3. Open the project

Open your browser and navigate to http://localhost:8000

## Notes on deployment

This project has never been used/tested in production. However to test it out, you'd need to run `yarn build` in the `astro` folder, and then `python3 manage.py collectstatic` in the django folder. You can then deploy the django project as you would normally do.
