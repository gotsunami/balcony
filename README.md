# balcony
An user administrable theme for django mezzanine

This mezzanine (http://mezzanine.jupo.org/) theme provides administration for the following elements:
- sliders
- badges
- argumentaries
- homepage containing these three models
- footers

They are integrated in the mezzanine admin.

# installation

requirements:
- django_ckeditor==5.0.3
- django-colorfield==0.1.10

```
  $ cd <my_mezzanine_dir>
  $ pip install django_ckeditor==5.0.3
  $ pip install django_colorfield==0.1.10
  $ git clone https://github.com/gotsunami/balcony.git
  $ python manage.py migrate balcony
  $ python manage.py collectstatic
```

Edit your `settings.py`, add `"ckeditor"` and `"balcony"` as the first entry in your `INSTALLED_APPS`:

```
INSTALLED_APPS = (
    "ckeditor",
    "colorfield",
    "balcony",
    "django.contrib.admin",
    "django.contrib.auth",
    ...
    "django.contrib.staticfiles",
    "mezzanine.boot",
    "mezzanine.conf",
    ...
)

```

Run the server for testing:

```
  $ python manage.py runserver
```

Or restart your webservice (probably nginx or apache).
