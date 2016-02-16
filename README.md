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

requirements: django_ckeditor==5.0.3

$ cd <my_mezzanine_dir>
$ pip install django_ckeditor==5.0.3
$ git clone https://github.com/gotsunami/balcony.git
$ python manage.py migrate balcony

Edit your settings.py and add "balcony" as the first entry in your INSTALLED_APPS.

Run the server for testing:

$ python manage.py runserver

Or restart your webservice (probably nginx or apache).
