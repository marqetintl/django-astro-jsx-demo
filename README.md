# django-astro-demo

This is a demo illustrating how to use [Astro](https://astro.build) with [Django](https://www.djangoproject.com/).

## Installation

1. Once in your work directory, clone this repo and navigate to it:

```bash
git clone https://github.com/marqetintl/django-astro-jsx-demo.git
cd django-astro-jsx-demo
```

2. Install dependencies

You'd need to install python and node dependencies. Note I am using `yarn`.

```bash
python3 -m venv env
pip3 install -r django/requirements.txt

cd astro
yarn
```

3. Run the project

```bash
yarn watch
```

Open a new terminal and run the django server

```bash
. env/bin/activate
cd django
python3 manage.py runserver
```

4. Open the project

Open your browser and navigate to http://localhost:8000

## Notes on deployment

This project is not ready for production. However to test it out, you'd need to run `yarn build` in the `astro` folder, and then `python3 manage.py collectstatic` in the django folder. You can then deploy the django project as you would normally do.
