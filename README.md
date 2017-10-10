# MyPythonProject
Contains Django and other python code

Using Database in django:
------------------------------

Create Model in app ( classes which define columns and field types )
Run makemigrations - python manage.py makemigration music
Run migration 	   - python manage.py migrate
This will populate db.sqllite with necessary date

Flow - Hit the app --> goes to settings --> check Installed Apps --> Goes to apps --> Goes to model
==================================================================================================

Create Table in Database:
------------------------
1. Open Shell using python manage.py shell
2. Import our class - from music.models import Album, Song
3. Check for our object = Album.objects.all() - This will get nothing as there are no entries yet
4. Make an entry like in object like a = Album(artist="Priyanka Chopra", album_title="Exotic", genre="Pitbull", album_logo="https://upload.wikimedia.org/wikipedia/en/f/f1/Exotic-Single-Cover.jpg")
5. Save it to database from shell using a.save()
6. Now you can view object like a.artist and a.id
